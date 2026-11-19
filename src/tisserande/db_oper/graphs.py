from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.graphs import Graph, GraphTemplate


class GraphTemplateOperations(TableOperations[GraphTemplate, models.GraphTemplate, models.GraphTemplateCreate]):
    """Table operations for graph templates."""


class GraphOperations(TableOperations[Graph, models.Graph, models.GraphCreate]):
    """Table operations for graph execution records."""


graph_template = GraphTemplateOperations(TableContext.from_db_class(GraphTemplate))
graph = GraphOperations(TableContext.from_db_class(Graph))
