from macon.local_sync.base import SyncOperations

from .. import models
from ..db.edges import EdgeTable
from ..local_async.edges import edge as edge_async


class EdgeSyncOperations(SyncOperations[EdgeTable, models.Edge, models.EdgeCreate]):
    """Synchronous operations for edges."""


edge = EdgeSyncOperations(edge_async)
