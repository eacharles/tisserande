"""ORM tables for AssocTemplate and Association.

``AssocTemplate`` records that a NodeTemplate is a participant in a
GraphTemplate.  ``Association`` records that a runtime Node participated
in an executed Graph.  Associations capture graph membership independently
of edges, so a node can belong to a graph without being directly connected
to another node.
"""

import uuid

from pydantic import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class AssocTemplate(Base):
    """ORM table for NodeTemplate ↔ GraphTemplate membership (int PK)."""

    __tablename__ = "assoc_template"

    id_: Mapped[int] = mapped_column(primary_key=True)
    node_template_id: Mapped[int] = mapped_column(ForeignKey("node_template.id_"), index=True)
    graph_template_id: Mapped[int] = mapped_column(ForeignKey("graph_template.id_"), index=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.AssocTemplateCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.AssocTemplate

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__


class Association(Base):
    """ORM table for Node ↔ Graph membership (composite UUID PK)."""

    __tablename__ = "association"

    node_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("node.uid_"), primary_key=True)
    graph_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("graph.uid_"), primary_key=True)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.AssociationCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.Association

    @classmethod
    def class_string(cls) -> str:
        return cls.__tablename__
