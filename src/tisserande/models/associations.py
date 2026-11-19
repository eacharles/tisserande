"""Pydantic models for associating nodes to graphs.

Two parallel sets of models exist:

* ``AssocTemplate`` — records that a NodeTemplate is a participant in a
  GraphTemplate (int FKs, int PK).
* ``Association`` — records that a runtime Node participated in an executed
  Graph (UUID FKs, no surrogate PK — the (node_id, graph_id) pair is the
  natural key).

Associations capture graph membership separately from edges so that a node
can be part of a graph without being directly connected to any other node
(e.g. an isolated configuration node attached to a graph for audit purposes).
"""

from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class AssocTemplateBase(BaseModel):
    """Base model for an association between a NodeTemplate and a GraphTemplate."""

    node_template_id: int = Field(..., description="Primary key of the NodeTemplate.")
    graph_template_id: int = Field(..., description="Primary key of the GraphTemplate.")


class AssocTemplateCreate(AssocTemplateBase):
    """Creation model for an AssocTemplate."""


class AssocTemplate(AssocTemplateBase):
    """AssocTemplate response model — includes the database-assigned primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "node_template_id", "graph_template_id"]

    id_: int = Field(..., gt=0, description="Auto-incremented primary key.")


class AssociationBase(BaseModel):
    """Base model for an association between a runtime Node and an executed Graph."""

    node_id: UUID = Field(..., description="UUID of the Node.")
    graph_id: UUID = Field(..., description="UUID of the Graph.")


class AssociationCreate(AssociationBase):
    """Creation model for an Association."""


class Association(AssociationBase):
    """Association response model — keyed by the (node_id, graph_id) pair."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["node_id", "graph_id"]
