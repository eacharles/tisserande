"""ORM tables for GraphTemplate and Graph.

``GraphTemplate`` stores the structural definition of a computation (which
node templates participate and how they connect).  ``Graph`` records a single
execution of a GraphTemplate, capturing status, timing, and environment.
"""

import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import DateTime, ForeignKey, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base
from .utils import uuid7 as _uuid7


class GraphTemplate(Base):
    """ORM table for graph template definitions (int PK)."""

    __tablename__ = "graph_template"

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, unique=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    version: Mapped[str | None] = mapped_column(String(100), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.GraphTemplateCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.GraphTemplate

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class Graph(Base):
    """ORM base table for graph execution records (UUID7 PK).

    Plugins can extend this via joined-table inheritance with their own subtable.
    ``graph_type`` is the polymorphic discriminator.
    """

    __tablename__ = "graph"
    __mapper_args__ = {
        "polymorphic_on": "graph_type",
        "polymorphic_identity": "base",
        "with_polymorphic": "*",
    }

    uid_: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=_uuid7)
    graph_type: Mapped[str] = mapped_column(String(50), index=True, default="base")
    graph_template_id: Mapped[int | None] = mapped_column(
        ForeignKey("graph_template.id_"), nullable=True, index=True
    )
    status: Mapped[str] = mapped_column(String(20), default="pending")
    start_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    end_time: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    hostname: Mapped[str | None] = mapped_column(String(255), nullable=True)
    user: Mapped[str | None] = mapped_column(String(255), nullable=True)
    environment_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.GraphCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Graph

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
