import uuid

from pydantic import BaseModel
from sqlalchemy import JSON, Float, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column
from uuid_utils import uuid7

from .. import models
from .base import Base


class NodeTable(Base):
    __tablename__ = "node"

    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid7)
    type_: Mapped[str] = mapped_column(String(50), index=True)
    execution_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("execution.id_"), nullable=True, index=True,
    )

    path: Mapped[str | None] = mapped_column(String(1024), nullable=True)
    config_data: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    value_float: Mapped[float | None] = mapped_column(Float, nullable=True)
    value_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    arg_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    data_file_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("data_file_type.id_"), nullable=True,
    )
    config_file_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("config_file_type.id_"), nullable=True,
    )
    config_dict_type_id: Mapped[int | None] = mapped_column(
        ForeignKey("config_dict_type.id_"), nullable=True,
    )
    parameter_id: Mapped[int | None] = mapped_column(
        ForeignKey("parameter.id_"), nullable=True,
    )
    array_id: Mapped[int | None] = mapped_column(
        ForeignKey("array.id_"), nullable=True,
    )
    class_id: Mapped[int | None] = mapped_column(
        ForeignKey("class.id_"), nullable=True,
    )
    python_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("python_function.id_"), nullable=True,
    )
    member_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("member_function.id_"), nullable=True,
    )
    shell_function_id: Mapped[int | None] = mapped_column(
        ForeignKey("shell_function.id_"), nullable=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.NodeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Node

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
