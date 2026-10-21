from macon.local_async.base import LocalOperations

from .. import models
from ..db.nodes import Node
from ..db_oper.nodes import node as node_ops


class NodeLocalOperations(LocalOperations[Node, models.Node, models.AnyNodeCreate]):
    """Async session-managed operations for nodes."""


node = NodeLocalOperations(node_ops)
