"""Pydantic models for provenance graph nodes (data nodes and logic nodes)."""

from typing import Annotated, Any, ClassVar, Literal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .types import NodeType


class NodeBase(BaseModel):
    """Base model for all graph nodes."""

    type_: NodeType = Field(..., description="What type of node")

    @field_validator("type_", mode="before")
    @classmethod
    def _coerce_type(cls, v: Any) -> Any:
        if isinstance(v, str):
            return NodeType(v)
        return v



class Node(NodeBase):
    """Node response model — base table columns only."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "arg_name", "execution_id"]

    id_: UUID
    execution_id: UUID | None = None
    arg_name: str | None = None


# --- Typed node models ---


class _TypedNodeCreateMixin(BaseModel):
    """Common fields for all typed node creation models."""

    arg_name: str | None = None
    execution_id: UUID | None = None


class _TypedNodeResponseMixin(BaseModel):
    """Common fields for all typed node response models."""

    model_config = ConfigDict(from_attributes=True)

    id_: UUID
    execution_id: UUID | None = None
    arg_name: str | None = None


class DataFileNodeBase(NodeBase):
    """Model for a data file node."""

    type_: Literal[NodeType.DATA_FILE] = NodeType.DATA_FILE
    path: str = Field(..., description="Path to the data file")


class DataFileNodeCreate(DataFileNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a DataFileNode."""

    data_file_type_name: str | None = None
    data_file_type_id: int | None = None


class DataFileNode(DataFileNodeBase, _TypedNodeResponseMixin):
    """DataFileNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "path", "data_file_type_id"]

    data_file_type_id: int | None = None


class ConfigFileNodeBase(NodeBase):
    """Model for a config file node."""

    type_: Literal[NodeType.CONFIG_FILE] = NodeType.CONFIG_FILE
    path: str = Field(..., description="Path to the config file")


class ConfigFileNodeCreate(ConfigFileNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a ConfigFileNode."""

    config_file_type_name: str | None = None
    config_file_type_id: int | None = None


class ConfigFileNode(ConfigFileNodeBase, _TypedNodeResponseMixin):
    """ConfigFileNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "path", "config_file_type_id"]

    config_file_type_id: int | None = None


class ConfigDictNodeBase(NodeBase):
    """Model for a config dict node."""

    type_: Literal[NodeType.CONFIG_DICT] = NodeType.CONFIG_DICT
    config_data: dict[str, Any] = Field(..., description="Configuration data")


class ConfigDictNodeCreate(ConfigDictNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a ConfigDictNode."""

    config_dict_type_name: str | None = None
    config_dict_type_id: int | None = None


class ConfigDictNode(ConfigDictNodeBase, _TypedNodeResponseMixin):
    """ConfigDictNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "config_dict_type_id"]

    config_dict_type_id: int | None = None


class ParameterNodeBase(NodeBase):
    """Model for a parameter node."""

    type_: Literal[NodeType.PARAMETER] = NodeType.PARAMETER


class ParameterNodeCreate(ParameterNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a ParameterNode."""

    value_float: float | None = None
    value_json: Any | None = None
    parameter_name: str | None = None
    parameter_id: int | None = None


class ParameterNode(ParameterNodeBase, _TypedNodeResponseMixin):
    """ParameterNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "value_float", "parameter_id"]

    value_float: float | None = None
    value_json: Any | None = None
    parameter_id: int | None = None


class ArrayNodeBase(NodeBase):
    """Model for an array node."""

    type_: Literal[NodeType.ARRAY] = NodeType.ARRAY


class ArrayNodeCreate(ArrayNodeBase, _TypedNodeCreateMixin):
    """Fields used to create an ArrayNode."""

    value_json: list[float] | list[list[float]] | None = None
    array_name: str | None = None
    array_id: int | None = None


class ArrayNode(ArrayNodeBase, _TypedNodeResponseMixin):
    """ArrayNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "array_id"]

    value_json: list[float] | list[list[float]] | None = None
    array_id: int | None = None


class ObjectNodeBase(NodeBase):
    """Model for a python object node."""

    type_: Literal[NodeType.OBJECT] = NodeType.OBJECT


class ObjectNodeCreate(ObjectNodeBase, _TypedNodeCreateMixin):
    """Fields used to create an ObjectNode."""

    value_json: Any | None = None
    class_name: str | None = None
    class_id: int | None = None


class ObjectNode(ObjectNodeBase, _TypedNodeResponseMixin):
    """ObjectNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "class_id"]

    value_json: Any | None = None
    class_id: int | None = None


class PythonFunctionNodeBase(NodeBase):
    """Model for a python function node."""

    type_: Literal[NodeType.PYTHON_FUNCTION] = NodeType.PYTHON_FUNCTION


class PythonFunctionNodeCreate(PythonFunctionNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a PythonFunctionNode."""

    python_function_name: str | None = None
    python_function_id: int | None = None


class PythonFunctionNode(PythonFunctionNodeBase, _TypedNodeResponseMixin):
    """PythonFunctionNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "python_function_id"]

    python_function_id: int | None = None


class MemberFunctionNodeBase(NodeBase):
    """Model for a member function node."""

    type_: Literal[NodeType.MEMBER_FUNCTION] = NodeType.MEMBER_FUNCTION


class MemberFunctionNodeCreate(MemberFunctionNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a MemberFunctionNode."""

    member_function_name: str | None = None
    member_function_id: int | None = None


class MemberFunctionNode(MemberFunctionNodeBase, _TypedNodeResponseMixin):
    """MemberFunctionNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "member_function_id"]

    member_function_id: int | None = None


class ShellFunctionNodeBase(NodeBase):
    """Model for a shell function node."""

    type_: Literal[NodeType.SHELL_FUNCTION] = NodeType.SHELL_FUNCTION


class ShellFunctionNodeCreate(ShellFunctionNodeBase, _TypedNodeCreateMixin):
    """Fields used to create a ShellFunctionNode."""

    shell_function_name: str | None = None
    shell_function_id: int | None = None


class ShellFunctionNode(ShellFunctionNodeBase, _TypedNodeResponseMixin):
    """ShellFunctionNode response model."""

    col_names_for_table: ClassVar[list[str]] = ["id_", "type_", "shell_function_id"]

    shell_function_id: int | None = None


AnyNodeCreate = Annotated[
    DataFileNodeCreate
    | ConfigFileNodeCreate
    | ConfigDictNodeCreate
    | ParameterNodeCreate
    | ArrayNodeCreate
    | ObjectNodeCreate
    | PythonFunctionNodeCreate
    | MemberFunctionNodeCreate
    | ShellFunctionNodeCreate,
    Field(discriminator="type_"),
]

AnyNode = Annotated[
    DataFileNode
    | ConfigFileNode
    | ConfigDictNode
    | ParameterNode
    | ArrayNode
    | ObjectNode
    | PythonFunctionNode
    | MemberFunctionNode
    | ShellFunctionNode,
    Field(discriminator="type_"),
]
