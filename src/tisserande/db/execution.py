"""ORM model for the Execution table (one record per tracked function call)."""

import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import DateTime, Float, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base
from .utils import uuid7 as _uuid7


class ExecutionTable(Base):
    __tablename__ = "execution"

    id_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=_uuid7)
    function_node_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("node.id_"),
        nullable=True,
    )
    status: Mapped[str] = mapped_column(String(20), default="pending")
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[float | None] = mapped_column(Float, nullable=True)
    error_message: Mapped[str | None] = mapped_column(Text, nullable=True)
    error_traceback: Mapped[str | None] = mapped_column(Text, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.ExecutionCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Execution

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
