from macon.local_sync.base import SyncOperations

from .. import models
from ..db.nodes import NodeTable
from ..local_async.nodes import node as node_async


class NodeSyncOperations(SyncOperations[NodeTable, models.Node, models.NodeCreate]):
    """Synchronous operations for nodes."""


node = NodeSyncOperations(node_async)
