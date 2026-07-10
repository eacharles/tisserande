from macon.local_async.base import LocalOperations

from .. import models
from ..db.nodes import NodeTable
from ..db_oper.nodes import node as node_ops


class NodeLocalOperations(LocalOperations[NodeTable, models.Node, models.NodeCreate]):
    """Async session-managed operations for nodes."""


node = NodeLocalOperations(node_ops)
