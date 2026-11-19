"""ORM tables for EdgeTemplate and Edge.

``EdgeTemplate`` connects two NodeTemplates in a GraphTemplate.  ``arg_name``
records the parameter name the destination NodeTemplate exposes for this
connection.  ``Edge`` connects two runtime Nodes and optionally back-references
the EdgeTemplate it was instantiated from via ``edge_template_id``.
"""

import uuid

from pydantic import BaseModel
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class EdgeTemplate(Base):
    """ORM table for directed edges between NodeTemplates (int PK)."""

    __tablename__ = "edge_template"

    id_: Mapped[int] = mapped_column(primary_key=True)
    from_id: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), index=True)
    to_id: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), index=True)
    arg_name: Mapped[str | None] = mapped_column(String(255), nullable=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.EdgeTemplateCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.EdgeTemplate

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class Edge(Base):
    """ORM table for directed edges between runtime Nodes (int PK)."""

    __tablename__ = "edge"

    id_: Mapped[int] = mapped_column(primary_key=True)
    from_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), index=True)
    to_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), index=True)
    edge_template_id: Mapped[int | None] = mapped_column(
        ForeignKey("edge_template.id_"), nullable=True, index=True
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
