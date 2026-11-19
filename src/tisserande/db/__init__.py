"""ORM layer for the tisserande provenance database.

Public API surface — import ORM classes from here rather than from sub-modules.
All classes inherit from ``Base`` (re-exported from ``macon``).  Call
``init_db()`` once at startup to create all tables.
"""

from .associations import AssocTemplate, Association
from .base import Base, close_db, get_session, init_db
from .data_types import (
    ArrayType,
    ClassType,
    ConfigDictType,
    ConfigFileType,
    DataFileType,
    ParameterType,
)
from .edges import Edge, EdgeTemplate
from .function_types import MemberFunction, PythonFunction, ShellFunction
from .graphs import Graph, GraphTemplate
from .node_templates import NodeTemplate
from .nodes import (
    Array,
    ClassInstance,
    ConfigDict,
    ConfigFile,
    DataFile,
    MemberFunctionCall,
    Node,
    Parameter,
    PythonFunctionCall,
    ShellFunctionCall,
)

__all__ = [
    # Core
    "Base",
    "init_db",
    "get_session",
    "close_db",
    # NodeTemplate base + data type templates
    "NodeTemplate",
    "DataFileType",
    "ConfigFileType",
    "ConfigDictType",
    "ParameterType",
    "ArrayType",
    "ClassType",
    # Function type templates
    "PythonFunction",
    "MemberFunction",
    "ShellFunction",
    # GraphTemplate + Graph
    "GraphTemplate",
    "Graph",
    # Node base + data node instances
    "Node",
    "DataFile",
    "ConfigFile",
    "ConfigDict",
    "Parameter",
    "Array",
    "ClassInstance",
    # Function call instances
    "PythonFunctionCall",
    "MemberFunctionCall",
    "ShellFunctionCall",
    # Edges
    "EdgeTemplate",
    "Edge",
    # Associations
    "AssocTemplate",
    "Association",
]
