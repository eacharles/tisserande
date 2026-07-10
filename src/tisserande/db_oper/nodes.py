from typing import Any

from macon import db_funcs
from macon.db.base import ensure_base_inheritance
from macon.db_oper.base import TableContext, TableOperations
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from structlog import get_logger

from .. import models
from ..db import data_types as db_data
from ..db import function_types as db_func
from ..db.nodes import (
    ArrayNodeTable,
    ConfigDictNodeTable,
    ConfigFileNodeTable,
    DataFileNodeTable,
    MemberFunctionNodeTable,
    NodeTable,
    ObjectNodeTable,
    ParameterNodeTable,
    PythonFunctionNodeTable,
    ShellFunctionNodeTable,
)
from ..models.types import NodeType

logger = get_logger(__name__)

_TYPE_FK_MAP: dict[str, tuple[str, str, type]] = {
    NodeType.DATA_FILE.value: ("data_file_type_name", "data_file_type_id", db_data.DataFileTypeTable),
    NodeType.CONFIG_FILE.value: ("config_file_type_name", "config_file_type_id", db_data.ConfigFileTypeTable),
    NodeType.CONFIG_DICT.value: ("config_dict_type_name", "config_dict_type_id", db_data.ConfigDictTypeTable),
    NodeType.PARAMETER.value: ("parameter_name", "parameter_id", db_data.ParameterTable),
    NodeType.ARRAY.value: ("array_name", "array_id", db_data.ArrayTable),
    NodeType.OBJECT.value: ("class_name", "class_id", db_data.ClassTable),
    NodeType.PYTHON_FUNCTION.value: (
        "python_function_name",
        "python_function_id",
        db_func.PythonFunctionTable,
    ),
    NodeType.MEMBER_FUNCTION.value: (
        "member_function_name",
        "member_function_id",
        db_func.MemberFunctionTable,
    ),
    NodeType.SHELL_FUNCTION.value: (
        "shell_function_name",
        "shell_function_id",
        db_func.ShellFunctionTable,
    ),
}

_TYPE_DB_CLASS_MAP: dict[str, type[NodeTable]] = {
    NodeType.DATA_FILE.value: DataFileNodeTable,
    NodeType.CONFIG_FILE.value: ConfigFileNodeTable,
    NodeType.CONFIG_DICT.value: ConfigDictNodeTable,
    NodeType.PARAMETER.value: ParameterNodeTable,
    NodeType.ARRAY.value: ArrayNodeTable,
    NodeType.OBJECT.value: ObjectNodeTable,
    NodeType.PYTHON_FUNCTION.value: PythonFunctionNodeTable,
    NodeType.MEMBER_FUNCTION.value: MemberFunctionNodeTable,
    NodeType.SHELL_FUNCTION.value: ShellFunctionNodeTable,
}


class NodeOperations(TableOperations[NodeTable, models.Node, models.NodeCreate]):
    """Operations for the Node table with polymorphic dispatch and FK resolution."""

    async def get_create_kwargs(
        self,
        session: AsyncSession,
        **kwargs: Any,
    ) -> dict[str, Any]:
        type_value = kwargs.get("type_")
        if isinstance(type_value, NodeType):
            type_value = type_value.value
            kwargs["type_"] = type_value

        if type_value and type_value in _TYPE_FK_MAP:
            name_field, id_field, db_class = _TYPE_FK_MAP[type_value]
            name_val = kwargs.pop(name_field, None)
            id_val = kwargs.get(id_field)
            if name_val and not id_val:
                resolved_id, _ = await db_funcs.read.lookup_by_id_or_name(
                    db_class,
                    session,
                    None,
                    name_val,
                )
                kwargs[id_field] = resolved_id

        return kwargs

    async def create_row(
        self,
        session: AsyncSession,
        *,
        validate: bool = True,
        **kwargs: Any,
    ) -> NodeTable:
        """Create a node row, dispatching to the correct subclass table."""
        ensure_base_inheritance(self.ctx.db_class)

        logger.debug("Creating node row", fields=list(kwargs.keys()))

        if validate:
            try:
                self.ctx.create_class.model_validate(kwargs)
            except ValidationError as e:
                logger.warning("Validation failed in create_row", errors=e.errors())
                raise

        kwargs = await self.get_create_kwargs(session, **kwargs)

        type_value = kwargs.get("type_")
        db_class = _TYPE_DB_CLASS_MAP.get(type_value, NodeTable)  # type: ignore[arg-type]

        # Filter kwargs to only columns that exist on the target table
        valid_columns = {c.key for c in db_class.__table__.columns}
        # Also include inherited columns from parent
        if db_class is not NodeTable:
            valid_columns |= {c.key for c in NodeTable.__table__.columns}
        filtered_kwargs = {k: v for k, v in kwargs.items() if k in valid_columns}

        filtered_kwargs = await db_class.pre_create_hook(session, filtered_kwargs)

        row = db_class(**filtered_kwargs)
        session.add(row)
        await session.flush()
        return row


node = NodeOperations(TableContext.from_db_class(NodeTable))
