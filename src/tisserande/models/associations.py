"""Pydantic models for associating nodes to provenance graphs."""

from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AssocTemplateBase(BaseModel):
    """Model for associations a NodeTempalte to a GraphTemplate"""
    node_template_id: int = Field(..., description="NodeTemplate in question")
    graph_template_id: int = Field(..., description="GraphTemplate in question")


class AssocTemplateCreate(AssocTemplateBase):
    """Fields used to create am AssocTemplate that are not in the DB."""

    
class AssocTemplate(AssocTemplateBase):
    """EdgeTemplate response model."""



class AssociationBase(BaseModel):
    """Model for a graph edge connecting two Nodes."""

    node_id: UUID = Field(..., description="Node in question")
    graph_id: UUID = Field(..., description="Graph in question")


class AssociationCreate(AssociationBase):
    """Fields used to create an Edge."""


class Association(AssociationBase):
    """Association response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["from_id", "to_id"]
