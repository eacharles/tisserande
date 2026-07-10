from typing import Any

from macon import db_funcs
from macon.db_oper.base import TableContext, TableOperations
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models
from ..db import data_types as db_data
from ..db import function_types as db_func
from ..db.nodes import NodeTable
from ..models.types import NodeType

_TYPE_FK_MAP: dict[str, tuple[str, str, type]] = {
    NodeType.DATA_FILE.value: ("data_file_type_name", "data_file_type_id", db_data.DataFileTypeTable),
    NodeType.CONFIG_FILE.value: ("config_file_type_name", "config_file_type_id", db_data.ConfigFileTypeTable),
    NodeType.CONFIG_DICT.value: ("config_dict_type_name", "config_dict_type_id", db_data.ConfigDictTypeTable),
    NodeType.PARAMETER.value: ("parameter_name", "parameter_id", db_data.ParameterTable),
    NodeType.ARRAY.value: ("array_name", "array_id", db_data.ArrayTable),
    NodeType.OBJECT.value: ("class_name", "class_id", db_data.ClassTable),
    NodeType.PYTHON_FUNCTION.value: (
        "python_function_name", "python_function_id", db_func.PythonFunctionTable,
    ),
    NodeType.MEMBER_FUNCTION.value: (
        "member_function_name", "member_function_id", db_func.MemberFunctionTable,
    ),
    NodeType.SHELL_FUNCTION.value: (
        "shell_function_name", "shell_function_id", db_func.ShellFunctionTable,
    ),
}


class NodeOperations(TableOperations[NodeTable, models.Node, models.NodeCreate]):
    """Operations for the Node table with type-dependent FK resolution."""

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
                    db_class, session, None, name_val,
                )
                kwargs[id_field] = resolved_id

        return kwargs


node = NodeOperations(TableContext.from_db_class(NodeTable))
