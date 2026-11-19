from macon.local_sync.base import SyncOperations

from .. import models
from ..db.graphs import Graph, GraphTemplate
from ..local_async.graphs import graph as graph_async
from ..local_async.graphs import graph_template as graph_template_async


class GraphTemplateSyncOperations(
    SyncOperations[GraphTemplate, models.GraphTemplate, models.GraphTemplateCreate]
):
    """Synchronous operations for graph templates."""


class GraphSyncOperations(SyncOperations[Graph, models.Graph, models.GraphCreate]):
    """Synchronous operations for graph execution records."""


graph_template = GraphTemplateSyncOperations(graph_template_async)
graph = GraphSyncOperations(graph_async)
