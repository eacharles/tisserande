from pydantic import BaseModel
from sqlalchemy import Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class DataFileTypeTable(Base):
    __tablename__ = "data_file_type"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.DataFileTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.DataFileType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigFileTypeTable(Base):
    __tablename__ = "config_file_type"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigFileTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigFileType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ConfigDictTypeTable(Base):
    __tablename__ = "config_dict_type"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ConfigDictTypeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ConfigDictType

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ParameterTable(Base):
    __tablename__ = "parameter"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ParameterCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Parameter

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ArrayTable(Base):
    __tablename__ = "array"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    n_dim: Mapped[int] = mapped_column(Integer)
    shape: Mapped[list[int]] = mapped_column(JSON)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ArrayCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Array

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ClassTable(Base):
    __tablename__ = "class"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    module_: Mapped[str] = mapped_column(String(512))

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ClassCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Class

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
