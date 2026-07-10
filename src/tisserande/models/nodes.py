"""Pydantic models for provenance graph nodes (data nodes and logic nodes)."""

from typing import Any, ClassVar, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from .types import NodeType


class NodeBase(BaseModel):
    """Base model for all graph nodes."""

    type_: NodeType = Field(..., description="What type of node")


class NodeCreate(NodeBase):
    """Generic node creation model."""

    path: str | None = Field(default=None, description="File path (for file nodes)")
    config_data: dict[str, Any] | None = Field(
        default=None, description="Config data (for config dict nodes)"
    )
    value_float: float | None = Field(default=None, description="Float value (for parameter nodes)")
    value_json: Any | None = Field(
        default=None, description="JSON-serializable value (for array/object nodes)"
    )
    arg_name: str | None = Field(default=None, description="Argument name in function signature")

    data_file_type_name: str | None = None
    data_file_type_id: int | None = None
    config_file_type_name: str | None = None
    config_file_type_id: int | None = None
    config_dict_type_name: str | None = None
    config_dict_type_id: int | None = None
    parameter_name: str | None = None
    parameter_id: int | None = None
    array_name: str | None = None
    array_id: int | None = None
    class_name: str | None = None
    class_id: int | None = None
    python_function_name: str | None = None
    python_function_id: int | None = None
    member_function_name: str | None = None
    member_function_id: int | None = None
    shell_function_name: str | None = None
    shell_function_id: int | None = None


class Node(NodeBase):
    """Node response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "arg_name", "execution_id"]

    id_: UUID
    execution_id: UUID | None = None
    path: str | None = None
    config_data: dict[str, Any] | None = None
    value_float: float | None = None
    value_json: Any | None = None
    arg_name: str | None = None

    data_file_type_id: int | None = None
    config_file_type_id: int | None = None
    config_dict_type_id: int | None = None
    parameter_id: int | None = None
    array_id: int | None = None
    class_id: int | None = None
    python_function_id: int | None = None
    member_function_id: int | None = None
    shell_function_id: int | None = None


# --- Typed node creation helpers ---


class DataFileNodeBase(NodeBase):
    """Model for a data file node."""

    type_: Literal[NodeType.DATA_FILE] = NodeType.DATA_FILE
    path: str = Field(..., description="Path to the data file")


class DataFileNodeCreate(DataFileNodeBase):
    """Fields used to create a DataFileNode."""

    data_file_type_name: str | None = None
    data_file_type_id: int | None = None
    arg_name: str | None = None


class DataFileNode(DataFileNodeBase):
    """DataFileNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "path", "data_file_type_id"]

    id_: UUID
    data_file_type_id: int | None = None
    execution_id: UUID | None = None


class ConfigFileNodeBase(NodeBase):
    """Model for a config file node."""

    type_: Literal[NodeType.CONFIG_FILE] = NodeType.CONFIG_FILE
    path: str = Field(..., description="Path to the config file")


class ConfigFileNodeCreate(ConfigFileNodeBase):
    """Fields used to create a ConfigFileNode."""

    config_file_type_name: str | None = None
    config_file_type_id: int | None = None
    arg_name: str | None = None


class ConfigFileNode(ConfigFileNodeBase):
    """ConfigFileNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "path", "config_file_type_id"]

    id_: UUID
    config_file_type_id: int | None = None
    execution_id: UUID | None = None


class ConfigDictNodeBase(NodeBase):
    """Model for a config dict node."""

    type_: Literal[NodeType.CONFIG_DICT] = NodeType.CONFIG_DICT
    config_data: dict[str, Any] = Field(..., description="Configuration data")


class ConfigDictNodeCreate(ConfigDictNodeBase):
    """Fields used to create a ConfigDictNode."""

    config_dict_type_name: str | None = None
    config_dict_type_id: int | None = None
    arg_name: str | None = None


class ConfigDictNode(ConfigDictNodeBase):
    """ConfigDictNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "config_dict_type_id"]

    id_: UUID
    config_dict_type_id: int | None = None
    execution_id: UUID | None = None


class ParameterNodeBase(NodeBase):
    """Model for a parameter node."""

    type_: Literal[NodeType.PARAMETER] = NodeType.PARAMETER
    value_float: float = Field(..., description="The parameter value")


class ParameterNodeCreate(ParameterNodeBase):
    """Fields used to create a ParameterNode."""

    parameter_name: str | None = None
    parameter_id: int | None = None
    arg_name: str | None = None


class ParameterNode(ParameterNodeBase):
    """ParameterNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "value_float", "parameter_id"]

    id_: UUID
    parameter_id: int | None = None
    execution_id: UUID | None = None


class ArrayNodeBase(NodeBase):
    """Model for an array node."""

    type_: Literal[NodeType.ARRAY] = NodeType.ARRAY
    value_json: list[float] | list[list[float]] = Field(..., description="The array data as nested lists")


class ArrayNodeCreate(ArrayNodeBase):
    """Fields used to create an ArrayNode."""

    array_name: str | None = None
    array_id: int | None = None
    arg_name: str | None = None


class ArrayNode(ArrayNodeBase):
    """ArrayNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "array_id"]

    id_: UUID
    array_id: int | None = None
    execution_id: UUID | None = None


class ObjectNodeBase(NodeBase):
    """Model for a python object node."""

    type_: Literal[NodeType.OBJECT] = NodeType.OBJECT
    value_json: Any = Field(default=None, description="JSON-serializable representation of the object")


class ObjectNodeCreate(ObjectNodeBase):
    """Fields used to create an ObjectNode."""

    class_name: str | None = None
    class_id: int | None = None
    arg_name: str | None = None


class ObjectNode(ObjectNodeBase):
    """ObjectNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "class_id"]

    id_: UUID
    class_id: int | None = None
    execution_id: UUID | None = None


class PythonFunctionNodeBase(NodeBase):
    """Model for a python function node."""

    type_: Literal[NodeType.PYTHON_FUNCTION] = NodeType.PYTHON_FUNCTION


class PythonFunctionNodeCreate(PythonFunctionNodeBase):
    """Fields used to create a PythonFunctionNode."""

    python_function_name: str | None = None
    python_function_id: int | None = None


class PythonFunctionNode(PythonFunctionNodeBase):
    """PythonFunctionNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "python_function_id"]

    id_: UUID
    python_function_id: int | None = None
    execution_id: UUID | None = None


class MemberFunctionNodeBase(NodeBase):
    """Model for a member function node."""

    type_: Literal[NodeType.MEMBER_FUNCTION] = NodeType.MEMBER_FUNCTION


class MemberFunctionNodeCreate(MemberFunctionNodeBase):
    """Fields used to create a MemberFunctionNode."""

    member_function_name: str | None = None
    member_function_id: int | None = None


class MemberFunctionNode(MemberFunctionNodeBase):
    """MemberFunctionNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "member_function_id"]

    id_: UUID
    member_function_id: int | None = None
    execution_id: UUID | None = None


class ShellFunctionNodeBase(NodeBase):
    """Model for a shell function node."""

    type_: Literal[NodeType.SHELL_FUNCTION] = NodeType.SHELL_FUNCTION


class ShellFunctionNodeCreate(ShellFunctionNodeBase):
    """Fields used to create a ShellFunctionNode."""

    shell_function_name: str | None = None
    shell_function_id: int | None = None


class ShellFunctionNode(ShellFunctionNodeBase):
    """ShellFunctionNode response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "shell_function_id"]

    id_: UUID
    shell_function_id: int | None = None
    execution_id: UUID | None = None
