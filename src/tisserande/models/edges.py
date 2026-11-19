"""Pydantic models for directed edges in the provenance graph.

Two parallel sets of models exist:

* ``EdgeTemplate`` — connects two NodeTemplates in a GraphTemplate (int FKs,
  int PK).  ``arg_name`` records the parameter name that the destination
  NodeTemplate exposes for this connection, making data-flow roles explicit at
  the graph-template level.
* ``Edge`` — connects two runtime Nodes in an executed Graph (UUID FKs, int
  PK).  ``edge_template_id`` optionally references the EdgeTemplate this edge
  was instantiated from, linking runtime data flow back to the graph structure.

An edge always runs from a source node to a destination node.  In the
provenance DAG, data nodes feed into function nodes (inputs) and function
nodes feed into data nodes (outputs).
"""

from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class EdgeTemplateBase(BaseModel):
    """Base model for an edge connecting two NodeTemplates in a graph template.

    ``arg_name`` records the parameter name the destination NodeTemplate
    exposes for this connection (e.g. ``"input_catalog"``).  Storing it on
    the edge — rather than on the node — means the same NodeTemplate can play
    different roles in different graph templates without ambiguity.
    """

    from_id: int = Field(..., description="Primary key of the source NodeTemplate.")
    to_id: int = Field(..., description="Primary key of the destination NodeTemplate.")
    arg_name: str | None = Field(
        default=None,
        description=(
            "Parameter name the destination NodeTemplate exposes for this connection"
            " (e.g. 'input_catalog')."
        ),
    )


class EdgeTemplateCreate(EdgeTemplateBase):
    """Creation model for an EdgeTemplate."""


class EdgeTemplate(EdgeTemplateBase):
    """EdgeTemplate response model — includes the database-assigned primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "from_id", "to_id", "arg_name"]

    id_: int = Field(..., gt=0, description="Auto-incremented primary key.")


class EdgeBase(BaseModel):
    """Base model for an edge connecting two runtime Nodes in an executed graph.

    ``edge_template_id`` optionally references the EdgeTemplate this edge was
    instantiated from, linking the runtime data flow back to the graph
    structure defined in the template.
    """

    from_id: UUID = Field(..., description="UUID of the source Node.")
    to_id: UUID = Field(..., description="UUID of the destination Node.")
    edge_template_id: int | None = Field(
        default=None,
        description=(
            "Foreign key into the EdgeTemplate table."
            " Null if this edge was not instantiated from a template."
        ),
    )


class EdgeCreate(EdgeBase):
    """Creation model for an Edge."""


class Edge(EdgeBase):
    """Edge response model — includes the database-assigned primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "from_id", "to_id", "edge_template_id"]

    id_: int = Field(..., gt=0, description="Auto-incremented primary key.")
