from macon.local_sync.base import SyncOperations

from .. import models
from ..db.edges import Edge
from ..local_async.edges import edge as edge_async


class EdgeSyncOperations(SyncOperations[Edge, models.Edge, models.EdgeCreate]):
    """Synchronous operations for edges."""


edge = EdgeSyncOperations(edge_async)
