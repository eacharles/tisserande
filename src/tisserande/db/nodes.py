"""ORM tables for runtime Node instances.

``Node`` is the joined-table inheritance base; it holds shared columns for all
node instances.  Each concrete sub-type adds its own subtable with
type-specific columns.

Data node sub-types (each adds creator/timestamp fields plus type-specific
payload): ``DataFile``, ``ConfigFile``, ``ConfigDict``, ``Parameter``,
``Array``, ``ClassInstance``.

Function call sub-types (each adds execution-lifecycle fields plus
type-specific payload): ``PythonFunctionCall``, ``MemberFunctionCall``,
``ShellFunctionCall``.
"""

import uuid
from datetime import datetime
from typing import Any

from pydantic import BaseModel
from sqlalchemy import DateTime, ForeignKey, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, declared_attr, mapped_column

from .. import models
from .base import Base
from .utils import uuid7 as _uuid7


# ---------------------------------------------------------------------------
# Base Node table
# ---------------------------------------------------------------------------


class Node(Base):
    """ORM base table for all runtime Node instances (UUID7 PK).

    ``node_type`` is the joined-table inheritance discriminator; its values
    match ``NodeType`` enum strings.  ``node_template_id`` optionally links
    this instance to its reusable type definition.
    """

    __tablename__ = "node"
    __mapper_args__ = {
        "polymorphic_on": "node_type",
        "polymorphic_identity": "base",
        "with_polymorphic": "*",
    }

    uid_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=_uuid7)
    node_type: Mapped[str] = mapped_column(String(50), index=True)
    node_template_id: Mapped[int | None] = mapped_column(
        ForeignKey("node_template.id_"), nullable=True, index=True
    )

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


# ---------------------------------------------------------------------------
# Data node sub-types
# ---------------------------------------------------------------------------


class DataFile(Node):
    """ORM subtable for data file node instances."""

    __tablename__ = "data_file"
    __mapper_args__ = {"polymorphic_identity": "data_file"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    file_path: Mapped[str] = mapped_column(String(1024))
    file_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)
    hash_algorithm: Mapped[str | None] = mapped_column(String(20), nullable=True)
    file_size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.DataFileCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.DataFile

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigFile(Node):
    """ORM subtable for configuration file node instances."""

    __tablename__ = "config_file"
    __mapper_args__ = {"polymorphic_identity": "config_file"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    file_path: Mapped[str] = mapped_column(String(1024))
    file_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)
    hash_algorithm: Mapped[str | None] = mapped_column(String(20), nullable=True)
    file_size_bytes: Mapped[int | None] = mapped_column(Integer, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigFileCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigFile

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigDict(Node):
    """ORM subtable for configuration dictionary node instances."""

    __tablename__ = "config_dict"
    __mapper_args__ = {"polymorphic_identity": "config_dict"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    config_data: Mapped[dict] = mapped_column(JSON)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigDictCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigDict

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class Parameter(Node):
    """ORM subtable for scalar parameter node instances."""

    __tablename__ = "parameter"
    __mapper_args__ = {"polymorphic_identity": "parameter"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    value: Mapped[float] = mapped_column()
    units: Mapped[str | None] = mapped_column(String(100), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ParameterCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Parameter

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class Array(Node):
    """ORM subtable for array node instances."""

    __tablename__ = "array"
    __mapper_args__ = {"polymorphic_identity": "array"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    shape: Mapped[list] = mapped_column(JSON)
    dtype: Mapped[str | None] = mapped_column(String(50), nullable=True)
    file_path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    value_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ArrayCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Array

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ClassInstance(Node):
    """ORM subtable for Python class instance node instances."""

    __tablename__ = "class_instance"
    __mapper_args__ = {"polymorphic_identity": "class_instance"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    creator: Mapped[str] = mapped_column(String(255))
    create_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    update_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    delete_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    ctor_values_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ClassInstanceCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ClassInstance

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


# ---------------------------------------------------------------------------
# Function call sub-types
# ---------------------------------------------------------------------------


class PythonFunctionCall(Node):
    """ORM subtable for Python function call node instances."""

    __tablename__ = "python_function_call"
    __mapper_args__ = {"polymorphic_identity": "python_function_call"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    exception_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    exception_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    args_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    kwargs_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    return_value_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    source_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.PythonFunctionCallCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.PythonFunctionCall

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class MemberFunctionCall(Node):
    """ORM subtable for class method call node instances.

    ``instance_node_id`` is a self-referential FK to the ``node`` table,
    pointing to the ``ClassInstance`` node that was ``self`` for this call.
    ``inherit_condition`` is required because two FKs reference ``node.uid_``.
    """

    __tablename__ = "member_function_call"

    @declared_attr.directive
    def __mapper_args__(cls) -> dict[str, Any]:  # noqa: N805
        return {
            "polymorphic_identity": "member_function_call",
            "inherit_condition": cls.__table__.c.uid_ == Node.__table__.c.uid_,
        }

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    exception_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    exception_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    instance_node_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("node.uid_"), nullable=True, index=True
    )
    args_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    kwargs_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    return_value_json: Mapped[Any | None] = mapped_column(JSON, nullable=True)
    source_hash: Mapped[str | None] = mapped_column(String(128), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.MemberFunctionCallCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.MemberFunctionCall

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ShellFunctionCall(Node):
    """ORM subtable for shell script invocation node instances."""

    __tablename__ = "shell_function_call"
    __mapper_args__ = {"polymorphic_identity": "shell_function_call"}

    uid_: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="pending")
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    exception_type: Mapped[str | None] = mapped_column(String(255), nullable=True)
    exception_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    command: Mapped[str | None] = mapped_column(Text, nullable=True)
    return_code: Mapped[int | None] = mapped_column(Integer, nullable=True)
    stdout: Mapped[str | None] = mapped_column(Text, nullable=True)
    stderr: Mapped[str | None] = mapped_column(Text, nullable=True)
    working_dir: Mapped[str | None] = mapped_column(String(1024), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ShellFunctionCallCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ShellFunctionCall

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
