from macon.local_sync.base import SyncOperations

from .. import models
from ..db.edges import Edge, EdgeTemplate
from ..local_async.edges import edge as edge_async
from ..local_async.edges import edge_template as edge_template_async


class EdgeTemplateSyncOperations(SyncOperations[EdgeTemplate, models.EdgeTemplate, models.EdgeTemplateCreate]):
    """Synchronous operations for edge templates."""


class EdgeSyncOperations(SyncOperations[Edge, models.Edge, models.EdgeCreate]):
    """Synchronous operations for edges."""


edge_template = EdgeTemplateSyncOperations(edge_template_async)
edge = EdgeSyncOperations(edge_async)
