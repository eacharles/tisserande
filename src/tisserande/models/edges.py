from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class EdgeBase(BaseModel):
    """Model for a graph edge connecting two nodes."""

    from_id: UUID = Field(..., description="Node the edge is coming from")
    to_id: UUID = Field(..., description="Node the edge is going to")


class EdgeCreate(EdgeBase):
    """Fields used to create an Edge."""

    execution_id: UUID | None = Field(default=None, description="Execution this edge belongs to")


class Edge(EdgeBase):
    """Edge response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "from_id", "to_id", "execution_id"]

    id_: int = Field(..., gt=0)
    execution_id: UUID | None = None
