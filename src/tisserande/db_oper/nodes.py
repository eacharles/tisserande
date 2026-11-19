import enum
from typing import Any

from macon import db_funcs
from macon.db.base import ensure_base_inheritance
from macon.db_oper.base import TableContext, TableOperations
from pydantic import BaseModel, ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from .. import models
from ..db.node_templates import NodeTemplate
from ..db.nodes import (
    Array,
    ClassInstance,
    ConfigDict,
    ConfigFile,
    DataFile,
    MemberFunctionCall,
    Node,
    Parameter,
    PythonFunctionCall,
    ShellFunctionCall,
)
from ..models.types import NodeType

logger = get_logger(__name__)

_TYPE_DB_CLASS_MAP: dict[str, type[Node]] = {
    NodeType.DATA_FILE.value: DataFile,
    NodeType.CONFIG_FILE.value: ConfigFile,
    NodeType.CONFIG_DICT.value: ConfigDict,
    NodeType.PARAMETER.value: Parameter,
    NodeType.ARRAY.value: Array,
    NodeType.CLASS_INSTANCE.value: ClassInstance,
    NodeType.PYTHON_FUNCTION_CALL.value: PythonFunctionCall,
    NodeType.MEMBER_FUNCTION_CALL.value: MemberFunctionCall,
    NodeType.SHELL_FUNCTION_CALL.value: ShellFunctionCall,
}

_TYPE_CREATE_MODEL_MAP: dict[str, type[BaseModel]] = {
    NodeType.DATA_FILE.value: models.DataFileCreate,
    NodeType.CONFIG_FILE.value: models.ConfigFileCreate,
    NodeType.CONFIG_DICT.value: models.ConfigDictCreate,
    NodeType.PARAMETER.value: models.ParameterCreate,
    NodeType.ARRAY.value: models.ArrayCreate,
    NodeType.CLASS_INSTANCE.value: models.ClassInstanceCreate,
    NodeType.PYTHON_FUNCTION_CALL.value: models.PythonFunctionCallCreate,
    NodeType.MEMBER_FUNCTION_CALL.value: models.MemberFunctionCallCreate,
    NodeType.SHELL_FUNCTION_CALL.value: models.ShellFunctionCallCreate,
}


def register_node_type(
    type_value: str,
    db_class: type[Node],
    create_model: type[BaseModel],
) -> None:
    """Register an external node type for polymorphic dispatch.

    Call this once at package initialisation before any ``node.create_row()``
    calls are made.

    Parameters
    ----------
    type_value:
        The string discriminator stored in the ``node.node_type`` column,
        e.g. ``"ceci_file"``.
    db_class:
        The SQLAlchemy ORM subclass of :class:`Node` whose
        ``polymorphic_identity`` matches *type_value*.
    create_model:
        The pydantic ``*Create`` model used to validate kwargs before
        inserting into the database.
    """
    _TYPE_DB_CLASS_MAP[type_value] = db_class
    _TYPE_CREATE_MODEL_MAP[type_value] = create_model


class NodeOperations(TableOperations[Node, models.Node, models.NodeCreate]):
    """Operations for the Node table with polymorphic dispatch and FK resolution."""

    async def get_create_kwargs(
        self,
        session: AsyncSession,
        **kwargs: Any,
    ) -> dict[str, Any]:
        # Coerce all enum values to their string/value representation for SQLAlchemy.
        for key in list(kwargs.keys()):
            if isinstance(kwargs[key], enum.Enum):
                kwargs[key] = kwargs[key].value

        node_template_name = kwargs.pop("node_template_name", None)
        if node_template_name and not kwargs.get("node_template_id"):
            resolved_id, _ = await db_funcs.read.lookup_by_id_or_name(
                NodeTemplate,
                session,
                None,
                node_template_name,
            )
            kwargs["node_template_id"] = resolved_id

        return kwargs

    async def create_row(
        self,
        session: AsyncSession,
        *,
        validate: bool = True,
        **kwargs: Any,
    ) -> Node:
        """Create a node row, dispatching to the correct subclass table."""
        ensure_base_inheritance(self.ctx.db_class)

        logger.debug("Creating node row", fields=list(kwargs.keys()))

        if validate:
            try:
                type_value = kwargs.get("node_type")
                if isinstance(type_value, NodeType):
                    type_value = type_value.value
                create_model = _TYPE_CREATE_MODEL_MAP.get(type_value)  # type: ignore[arg-type]
                if create_model is not None:
                    create_model.model_validate(kwargs)
            except ValidationError as e:
                logger.warning("Validation failed in create_row", errors=e.errors())
                raise

        kwargs = await self.get_create_kwargs(session, **kwargs)

        type_value = kwargs.get("node_type")
        db_class = _TYPE_DB_CLASS_MAP.get(type_value, Node)  # type: ignore[arg-type]

        # Collect columns from all levels of the inheritance hierarchy.
        valid_columns: set[str] = set()
        for klass in db_class.__mro__:
            tbl = getattr(klass, "__table__", None)
            if tbl is not None:
                valid_columns |= {c.key for c in tbl.columns}
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_columns}

        filtered_kwargs = await db_class.pre_create_hook(session, filtered_kwargs)

        row = db_class(**filtered_kwargs)
        session.add(row)
        await session.flush()
        return row


node = NodeOperations(TableContext.from_db_class(Node))
