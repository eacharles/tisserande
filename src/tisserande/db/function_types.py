"""ORM models for function type tables (PythonFunction, MemberFunction, ShellFunction)."""

from pydantic import BaseModel
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class PythonFunctionTable(Base):
    __tablename__ = "python_function"
    __table_args__ = (UniqueConstraint("name", "module_", name="uq_python_function_name_module"),)

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    module_: Mapped[str] = mapped_column(String(512))

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.PythonFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.PythonFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class MemberFunctionTable(Base):
    __tablename__ = "member_function"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("class.id_"), index=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.MemberFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.MemberFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ShellFunctionTable(Base):
    __tablename__ = "shell_function"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ShellFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ShellFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
