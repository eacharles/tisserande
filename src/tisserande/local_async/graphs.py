from macon.local_async.base import LocalOperations

from .. import models
from ..db.graphs import Graph, GraphTemplate
from ..db_oper.graphs import graph as graph_ops
from ..db_oper.graphs import graph_template as graph_template_ops


class GraphTemplateLocalOperations(
    LocalOperations[GraphTemplate, models.GraphTemplate, models.GraphTemplateCreate]
):
    """Async session-managed operations for graph templates."""


class GraphLocalOperations(LocalOperations[Graph, models.Graph, models.GraphCreate]):
    """Async session-managed operations for graph execution records."""


graph_template = GraphTemplateLocalOperations(graph_template_ops)
graph = GraphLocalOperations(graph_ops)
