"""ORM base table for NodeTemplate (reusable node type definitions).

All concrete NodeTemplate sub-types inherit from ``NodeTemplate`` via
SQLAlchemy joined-table inheritance.  The ``node_template_type`` column
acts as the polymorphic discriminator; its values match the
``NodeTemplateType`` enum strings defined in ``models/types.py``.
"""

from typing import Any

from pydantic import BaseModel
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .. import models
from .base import Base


class NodeTemplate(Base):
    """Base ORM table for all NodeTemplate sub-types.

    Shared columns live here; type-specific columns live in subtables that
    JOIN to this one on ``id_``.  ``with_polymorphic: "*"`` causes SQLAlchemy
    to load all subtable columns in a single query via outer joins.
    """

    __tablename__ = "node_template"
    __mapper_args__ = {
        "polymorphic_on": "node_template_type",
        "polymorphic_identity": "base",
        "with_polymorphic": "*",
    }

    id_: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    node_template_type: Mapped[str] = mapped_column(String(50), index=True)
    version: Mapped[str] = mapped_column(String(100))
    is_superseded: Mapped[bool] = mapped_column(default=False)

    @classmethod
    def pydantic_create_class(cls) -> type[BaseModel]:
        return models.NodeTemplateCreate

    @classmethod
    def pydantic_model_class(cls) -> type[BaseModel]:
        return models.NodeTemplate

    @classmethod
    def class_string(cls) -> str:
        return "node_template"

    @classmethod
    def to_pydantic(cls, row: Any) -> BaseModel:
        pydantic_class = type(row).pydantic_model_class()
        return pydantic_class.model_validate(row, from_attributes=True)
