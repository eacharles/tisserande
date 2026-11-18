"""Pydantic models for provenance graph edges connecting nodes."""

from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class EdgeTemplateBase(BaseModel):
    """Model for a graph edge connecting two NodeTemplates."""
    from_id: int = Field(..., description="Node the edge is coming from")
    to_id: int = Field(..., description="Node the edge is going to")


class EdgeTemplateCreate(EdgeTemplateBase):
    """Fields used to create am EdgeTemplate that are not in the DB."""

    
class EdgeTemplate(EdgeTemplateBase):
    """EdgeTemplate response model."""



class EdgeBase(BaseModel):
    """Model for a graph edge connecting two Nodes."""

    from_id: UUID = Field(..., description="Node the edge is coming from")
    to_id: UUID = Field(..., description="Node the edge is going to")


class EdgeCreate(EdgeBase):
    """Fields used to create an Edge."""


class Edge(EdgeBase):
    """Edge response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["from_id", "to_id"]
