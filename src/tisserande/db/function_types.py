"""ORM tables for function-type NodeTemplate sub-types.

Each class inherits from ``NodeTemplate`` via SQLAlchemy joined-table
inheritance and corresponds to one value of ``NodeTemplateType``.
``PythonFunction`` and ``ShellFunction`` are independent sub-types;
``MemberFunction`` additionally carries a FK to the ``ClassType`` that owns
the method.
"""

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from pydantic import BaseModel

from .. import models
from .node_templates import NodeTemplate


class PythonFunction(NodeTemplate):
    """ORM table for the PythonFunction node template sub-type."""

    __tablename__ = "python_function"
    __mapper_args__ = {"polymorphic_identity": "python_function"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    module_: Mapped[str] = mapped_column(String(255))
    is_async: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.PythonFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.PythonFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class MemberFunction(NodeTemplate):
    """ORM table for the MemberFunction node template sub-type.

    ``class_id`` is a FK to the ``class_type`` table that owns this method.
    It allows queries like "find all methods belonging to this Python class".
    """

    __tablename__ = "member_function"
    __mapper_args__ = {"polymorphic_identity": "member_function"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("class_type.id_"), index=True)
    is_async: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.MemberFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.MemberFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class ShellFunction(NodeTemplate):
    """ORM table for the ShellFunction node template sub-type."""

    __tablename__ = "shell_function"
    __mapper_args__ = {"polymorphic_identity": "shell_function"}

    id_: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), primary_key=True)
    script_path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    interpreter: Mapped[str | None] = mapped_column(String(100), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ShellFunctionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.ShellFunction

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
