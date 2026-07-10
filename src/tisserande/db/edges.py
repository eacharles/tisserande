"""ORM model for the Edge table (directed links between nodes in the provenance DAG)."""

import uuid

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class EdgeTable(Base):
    __tablename__ = "edge"

    id_: Mapped[int] = mapped_column(primary_key=True)
    from_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), index=True)
    to_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.id_"), index=True)
    execution_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("execution.id_"), nullable=True, index=True,
    )

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.EdgeCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Edge

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
