"""Base Pydantic models for the tisserande provenance graph.

Defines two parallel hierarchies:

Template hierarchy (reusable type definitions, stored with int PKs):
  NodeTemplate  ──┬── DataNodeTemplate  (data sources/sinks)
                  └── FunctionNodeTemplate  (computational steps)
  GraphTemplate

Instance hierarchy (runtime execution records, stored with UUID7 PKs):
  Node  ──┬── DataNode  (produced/consumed data)
          └── FunctionNode  (function call records)
  Graph

Each concrete sub-type is built by combining the appropriate base class with a
plain mixin class that adds type-specific fields and sets the discriminator
(node_template_type or node_type) as a Literal.
"""

from datetime import datetime
from typing import Any, ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .types import ExecutionStatus, NodeTemplateType, NodeType


# ---------------------------------------------------------------------------
# NodeTemplate hierarchy
# ---------------------------------------------------------------------------


class NodeTemplateBase(BaseModel):
    """Shared fields for all NodeTemplate sub-types.

    A NodeTemplate is a reusable type definition for a node.  It captures
    metadata that is common across all executions that involve this kind of
    node (e.g. every call to the same Python function, or every use of a
    particular data file schema).  NodeTemplates are stored once and
    referenced by zero or more runtime Nodes.
    """

    name: str = Field(..., description="Human-readable name. Should be unique within a node_template_type.")
    node_template_type: NodeTemplateType = Field(..., description="Discriminator identifying the sub-type of this template.")
    version: str = Field(..., description="Version string for this template.")
    is_superseded: bool = Field(default=False, description="True if a newer version of this template exists.")

    @field_validator("node_template_type", mode="before")
    @classmethod
    def _coerce_node_template_type(cls, v: Any) -> Any:
        if isinstance(v, str):
            return NodeTemplateType(v)
        return v


class NodeTemplateCreate(NodeTemplateBase):
    """Fields required to create a new NodeTemplate record."""


class NodeTemplate(NodeTemplateBase):
    """NodeTemplate response model — includes the database-assigned primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "version", "is_superseded"]

    id_: int = Field(..., gt=0, description="Auto-incremented primary key.")


class DataNodeTemplateMixin:
    """Mixin for data-type NodeTemplate sub-classes.

    Data node templates describe sources and sinks of data (files, parameters,
    arrays, class instances) rather than computational steps.  Concrete
    sub-types add type-specific fields and set
    ``node_template_type`` to the appropriate ``Literal``.
    """


class DataNodeTemplateCreate(NodeTemplateCreate, DataNodeTemplateMixin):
    """Creation model for data-type node templates."""


class DataNodeTemplate(NodeTemplate, DataNodeTemplateMixin):
    """Response model for data-type node templates."""


class FunctionNodeTemplateMixin:
    """Mixin for function-type NodeTemplate sub-classes.

    Function node templates describe computational steps (Python functions,
    class methods, shell scripts) rather than data.  Concrete sub-types add
    type-specific fields and set ``node_template_type`` to the appropriate
    ``Literal``.
    """


class FunctionNodeTemplateCreate(NodeTemplateCreate, FunctionNodeTemplateMixin):
    """Creation model for function-type node templates."""


class FunctionNodeTemplate(NodeTemplate, FunctionNodeTemplateMixin):
    """Response model for function-type node templates."""


# ---------------------------------------------------------------------------
# GraphTemplate
# ---------------------------------------------------------------------------


class GraphTemplateBase(BaseModel):
    """Shared fields for all GraphTemplate records.

    A GraphTemplate describes the structure of a computation — which node
    templates participate and how they are connected — independently of any
    particular execution.  When a graph is actually run, a concrete Graph
    instance is created from this template.

    ``version`` follows the same semantics as ``NodeTemplateBase.version``:
    it identifies which revision of the graph structure produced a given set
    of results.  ``description`` is a free-text summary suitable for display
    in a provenance UI.
    """

    name: str = Field(..., description="Human-readable name for this graph template. Should be unique.")
    description: str | None = Field(default=None, description="Optional free-text description of what this graph computes.")
    version: str | None = Field(default=None, description="Version string for this graph template.")


class GraphTemplateCreate(GraphTemplateBase):
    """Fields required to create a new GraphTemplate record."""


class GraphTemplate(GraphTemplateBase):
    """GraphTemplate response model — includes the database-assigned primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "version"]

    id_: int = Field(..., gt=0, description="Auto-incremented primary key.")


# ---------------------------------------------------------------------------
# Node hierarchy
# ---------------------------------------------------------------------------


class NodeBase(BaseModel):
    """Shared fields for all runtime Node instances.

    Nodes are the vertices of the provenance DAG produced by an actual
    execution.  Each node may optionally reference a NodeTemplate that
    provides shared type metadata.
"""

    node_template_id: int | None = Field(None, description="Foreign key into the NodeTemplate table. Null if no template was registered.")
    node_type: NodeType = Field(..., description="Discriminator identifying the sub-type of this node.")

    @field_validator("node_type", mode="before")
    @classmethod
    def _coerce_node_type(cls, v: Any) -> Any:
        if isinstance(v, str):
            return NodeType(v)
        return v


class NodeCreate(NodeBase):
    """Fields required to create a new Node record."""


class Node(NodeBase):
    """Node response model — includes the database-assigned UUID primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["uid_", "node_type", "node_template_id"]

    uid_: UUID = Field(..., description="UUID7 primary key (time-ordered).")


class DataNodeMixin:
    """Mixin for data-type Node sub-classes.

    Adds provenance metadata fields tracking who created the data and when it
    was created, updated, or deleted.  Concrete sub-types add type-specific
    fields and set ``node_type`` to the appropriate ``Literal``.
    """

    creator: str = Field(..., description="Identifier of who or what created this data (e.g. username or process name).")
    create_time: datetime | None = Field(default=None, description="When this data was created.")
    update_time: datetime | None = Field(default=None, description="When this data was last updated.")
    delete_time: datetime | None = Field(default=None, description="When this data was deleted, if applicable.")


class DataNodeCreate(NodeCreate, DataNodeMixin):
    """Creation model for data-type nodes."""


class DataNode(Node, DataNodeMixin):
    """Response model for data-type nodes."""


class FunctionNodeMixin:
    """Mixin for function-type Node sub-classes.

    Adds execution lifecycle fields covering status, timing, and failure
    details.  ``exception_type`` and ``exception_message`` capture failure
    information on the node itself so a single query surfaces both timing and
    error context.

    Concrete sub-types set ``node_type`` to the appropriate ``Literal``.
    """

    status: ExecutionStatus = Field(default=ExecutionStatus.PENDING, description="Execution status of this function call.")
    start_time: datetime | None = Field(default=None, description="When execution started.")
    end_time: datetime | None = Field(default=None, description="When execution ended.")
    exception_type: str | None = Field(default=None, description="Fully-qualified exception class name if the call failed (e.g. 'ValueError').")
    exception_message: str | None = Field(default=None, description="Exception message string if the call failed.")


class FunctionNodeCreate(NodeCreate, FunctionNodeMixin):
    """Creation model for function-type nodes."""


class FunctionNode(Node, FunctionNodeMixin):
    """Response model for function-type nodes."""


# ---------------------------------------------------------------------------
# Graph
# ---------------------------------------------------------------------------


class GraphBase(BaseModel):
    """Shared fields for all runtime Graph instances.

    A Graph is a provenance record for a single execution of a GraphTemplate.
    It tracks the overall execution status, wall-clock timing, and the
    execution environment so results can be reproduced or attributed.

    ``hostname`` and ``user`` record where and by whom the graph was run.
    ``environment_json`` captures relevant environment variables (e.g. software
    versions, pipeline settings) at run time as a string-to-string mapping.
    """

    graph_template_id: int = Field(..., description="Foreign key into the GraphTemplate table.")
    status: ExecutionStatus = Field(default=ExecutionStatus.PENDING, description="Overall execution status of this graph.")
    start_time: datetime | None = Field(default=None, description="When execution of this graph started.")
    end_time: datetime | None = Field(default=None, description="When execution of this graph ended.")
    hostname: str | None = Field(default=None, description="Hostname of the machine on which this graph ran.")
    user: str | None = Field(default=None, description="Username or identifier of who initiated this graph run.")
    environment_json: dict[str, str] | None = Field(default=None, description="Snapshot of relevant environment variables at run time (string → string mapping).")


class GraphCreate(GraphBase):
    """Fields required to create a new Graph record."""


class Graph(GraphBase):
    """Graph response model — includes the database-assigned UUID primary key."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["uid_", "graph_template_id", "status", "start_time", "end_time", "hostname", "user"]

    uid_: UUID = Field(..., description="UUID7 primary key (time-ordered).")
