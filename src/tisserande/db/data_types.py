"""ORM tables for data-type NodeTemplate sub-types.

Each class inherits from ``NodeTemplate`` via SQLAlchemy joined-table
inheritance and corresponds to one value of ``NodeTemplateType``.  The
``polymorphic_identity`` must match the enum string exactly.
"""

from sqlalchemy import ForeignKey, JSON, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from .. import models
from .node_templates import NodeTemplate


class DataFileType(NodeTemplate):
    """ORM table for the DataFileType node template sub-type."""

    __tablename__ = "data_file_type"
    __mapper_args__ = {"polymorphic_identity": "data_file_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    file_format: Mapped[str | None] = mapped_column(String(100), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.DataFileTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.DataFileType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigFileType(NodeTemplate):
    """ORM table for the ConfigFileType node template sub-type."""

    __tablename__ = "config_file_type"
    __mapper_args__ = {"polymorphic_identity": "config_file_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigFileTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigFileType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigDictType(NodeTemplate):
    """ORM table for the ConfigDictType node template sub-type."""

    __tablename__ = "config_dict_type"
    __mapper_args__ = {"polymorphic_identity": "config_dict_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    default_config: Mapped[dict] = mapped_column(JSON)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigDictTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigDictType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ParameterType(NodeTemplate):
    """ORM table for the ParameterType node template sub-type."""

    __tablename__ = "parameter_type"
    __mapper_args__ = {"polymorphic_identity": "parameter_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    units: Mapped[str | None] = mapped_column(String(100), nullable=True)
    dtype: Mapped[str | None] = mapped_column(String(50), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ParameterTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ParameterType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ArrayType(NodeTemplate):
    """ORM table for the ArrayType node template sub-type."""

    __tablename__ = "array_type"
    __mapper_args__ = {"polymorphic_identity": "array_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    dtype: Mapped[str | None] = mapped_column(String(50), nullable=True)
    units: Mapped[str | None] = mapped_column(String(100), nullable=True)
    ndim: Mapped[int | None] = mapped_column(nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ArrayTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ArrayType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ClassType(NodeTemplate):
    """ORM table for the Class (Python class type) node template sub-type.

    The ``__tablename__`` is ``"class_type"`` to avoid colliding with SQLite's
    reserved word ``class``.  The ``polymorphic_identity`` is ``"class_type"``
    to match ``NodeTemplateType.CLASS_TYPE``.
    """

    __tablename__ = "class_type"
    __mapper_args__ = {"polymorphic_identity": "class_type"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    module_: Mapped[str] = mapped_column(String(255))

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ClassCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Class

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
