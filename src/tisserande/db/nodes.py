"""ORM models for provenance graph nodes using joined-table inheritance.

Base NodeTable holds shared columns (id, type discriminator, execution_id, arg_name).
Each node type has its own subtable with type-specific columns. Edges and executions
still FK to the base node table, keeping graph queries simple.
"""

from __future__ import annotations

import uuid
from typing import Any

from pydantic import BaseModel
from sqlalchemy import JSON, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base
from .utils import uuid7 as _uuid7


class NodeTable(Base):
    """Base ORM table for all provenance graph nodes."""

    __tablename__ = "node"
    __mapper_args__ = {
        "polymorphic_on": "type_",
        "polymorphic_identity": "base",
        "with_polymorphic": "*",
    }

    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=_uuid7)
    type_: Mapped[str] = mapped_column(String(50), index=True)
    execution_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("execution.id_"),
        nullable=True,
        index=True,
    )
    arg_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.NodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Node

    @classmethod
    def class_string(cls) -> str:
        return "node"

    @classmethod
    def to_pydantic(cls, row: Any) -> BaseModel:
        pydantic_class = type(row).pydantic_model_class()
        return pydantic_class.model_validate(row, from_attributes=True)


class DataFileNodeTable(NodeTable):
    """ORM table for data file nodes."""

    __tablename__ = "data_file_node"
    __mapper_args__ = {"polymorphic_identity": "data_file"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    data_file_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("data_file_type.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.DataFileNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.DataFileNode

    @classmethod
    def class_string(cls) -> str:
        return "data_file_node"


class ConfigFileNodeTable(NodeTable):
    """ORM table for config file nodes."""

    __tablename__ = "config_file_node"
    __mapper_args__ = {"polymorphic_identity": "config_file"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    config_file_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("config_file_type.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigFileNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigFileNode

    @classmethod
    def class_string(cls) -> str:
        return "config_file_node"


class ConfigDictNodeTable(NodeTable):
    """ORM table for config dict nodes."""

    __tablename__ = "config_dict_node"
    __mapper_args__ = {"polymorphic_identity": "config_dict"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    config_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    config_dict_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("config_dict_type.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigDictNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigDictNode

    @classmethod
    def class_string(cls) -> str:
        return "config_dict_node"


class ParameterNodeTable(NodeTable):
    """ORM table for parameter nodes."""

    __tablename__ = "parameter_node"
    __mapper_args__ = {"polymorphic_identity": "parameter"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    value_float: Mapped[float | None] = mapped_column(Float, nullable=True)
    value_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    parameter_id: Mapped[int | None] = mapped_column(
        ForeignKey("parameter.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ParameterNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ParameterNode

    @classmethod
    def class_string(cls) -> str:
        return "parameter_node"


class ArrayNodeTable(NodeTable):
    """ORM table for array nodes."""

    __tablename__ = "array_node"
    __mapper_args__ = {"polymorphic_identity": "array"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    value_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    array_id: Mapped[int | None] = mapped_column(
        ForeignKey("array.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ArrayNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ArrayNode

    @classmethod
    def class_string(cls) -> str:
        return "array_node"


class ObjectNodeTable(NodeTable):
    """ORM table for object nodes."""

    __tablename__ = "object_node"
    __mapper_args__ = {"polymorphic_identity": "object"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    value_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    class_id: Mapped[int | None] = mapped_column(
        ForeignKey("class.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ObjectNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ObjectNode

    @classmethod
    def class_string(cls) -> str:
        return "object_node"


class PythonFunctionNodeTable(NodeTable):
    """ORM table for python function nodes."""

    __tablename__ = "python_function_node"
    __mapper_args__ = {"polymorphic_identity": "python_function"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    python_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("python_function.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.PythonFunctionNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.PythonFunctionNode

    @classmethod
    def class_string(cls) -> str:
        return "python_function_node"


class MemberFunctionNodeTable(NodeTable):
    """ORM table for member function nodes."""

    __tablename__ = "member_function_node"
    __mapper_args__ = {"polymorphic_identity": "member_function"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    member_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("member_function.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.MemberFunctionNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.MemberFunctionNode

    @classmethod
    def class_string(cls) -> str:
        return "member_function_node"


class ShellFunctionNodeTable(NodeTable):
    """ORM table for shell function nodes."""

    __tablename__ = "shell_function_node"
    __mapper_args__ = {"polymorphic_identity": "shell_function"}

    id_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), primary_key=True)
    shell_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("shell_function.id_"),
        nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ShellFunctionNodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ShellFunctionNode

    @classmethod
    def class_string(cls) -> str:
        return "shell_function_node"
