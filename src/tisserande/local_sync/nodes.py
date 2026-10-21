from macon.local_sync.base import SyncOperations

from .. import models
from ..db.nodes import Node
from ..local_async.nodes import node as node_async


class NodeSyncOperations(SyncOperations[Node, models.Node, models.AnyNodeCreate]):
    """Synchronous operations for nodes."""


node = NodeSyncOperations(node_async)
