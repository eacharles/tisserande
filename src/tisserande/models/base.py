"""Pydantic models for data-related type tables (DataFileType, ConfigFileType, etc.)."""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class NodeTemplateBase(BaseModel):
    """Base class for templates of Nodes

    These are used as placeholders in graphs that
    could be run. 

    Actually running a graph should create Nodes, rather than
    NodeTemplates.

    NodeTemplate is to here to store generic information about all
    the nodes of a particular type.
    """

    name: str = Field(..., description="Name the type of Node.  Should be unique.")
    node_type: str = Field(..., description="Type of node.  Should be a sub-class of NodeTemplate.")


class NodeTemplateCreate(NodeTemplateBase):
    """Includes fields used to create a NodeTemplate that are not in the DB."""


class NodeTemplate(NodeTemplateBase):
    """NodeTemplate response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0, description="Unique ID for this NodeTemplate")


class DataNodeTemplateMixin:
    """Mixin class for all data-type NodeTemplate sub-classes """


class DataNodeTemplateCreate(NodeTemplateCreate, DataNodeTemplateMixin):
    """Includes fields used to create a DataNodeTemplate that are not in the DB."""


class DataNodeTemplate(NodeTemplate, DataNodeTemplateMixin):
    """DataNodeTemplate response model"""
    
    
    
class FunctionNodeTemplateMixin(NodeTemplateBase):
    """Mixin class for all function-type NodeTemplate sub-classes """


class FunctionNodeTemplateCreate(NodeTemplateCreate, FunctionNodeTemplateMixin):
    """Includes fields used to create a FunctionNodeTemplate that are not in the DB."""


class FunctionNodeTemplate(NodeTemplate, FunctionNodeTemplateMixin):
    """FunctionNodeTemplate response model"""
    


class GraphTemplateBase(BaseModel):
    """Base class for templates of Graphs 

    These are used as placeholders for Graphs that could be run.

    Actually running a graph should create Graph objects.

    GraphTemplate is to store generic information about all
    the graphs of a particular type.
    """

    name: str = Field(..., description="Name the type of Node.  Should be unique.")


class GraphTemplateCreate(GraphTemplateBase):
    """Fields used to create a GraphTemplate."""


class GraphTemplate(GraphTemplateBase):
    """GraphTemplate response model"""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0, description="Unique ID for this GraphTemplate")

    

class NodeBase(BaseModel):
    """Base class for all specific version of nodes

    These are nodes from graphs that have been run.
    """
    node_template_id: int | None = (..., description="Foreign key into NodeTemplate table")
    node_type: str = Field(..., description="Type of node.  Should be a sub-class of NodeTemplate.")


class NodeCreate(NodeBase):
    """Fields used to create a Node."""


class Node(NodeBase):
    """Node response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["uid_", "node_type", "node_template_id"]

    uid_: uuid7 = Field(..., description="UUID for this node")
    


class DataNodeMixin:
    """Mixin class for all data-type Node sub-classes. """


class DataNodeCreate(NodeCreate, DataNodeMixin):
    """Includes fields used to create a DataNode that are not in the DB."""


class DataNode(Node, DataNodeMixin):
    """DataNode response model."""


    
class FunctionNodeMixin:
    """Mixin class for all function-type Node sub-classes. """


class FunctionNodeCreate(NodeCreate, FunctionNodeMixin):
    """Includes fields used to create a FunctionNode that are not in the DB."""


class FunctionNode(Node, FunctionNodeMixin):
    """FunctionNode response model."""



class GraphBase(BaseModel):
    """Base class for Graphs"""


class GraphCreate(GraphBase):
    """Includes fields used to create a Graph that are not in the DB."""


class Graph(GraphBase):
    """Graph response model"""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["uid_", "node_type", "node_template_id"]

    uid_: uuid7 = Field(..., description="UUID for this node")
