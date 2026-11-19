from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.edges import Edge, EdgeTemplate


class EdgeTemplateOperations(TableOperations[EdgeTemplate, models.EdgeTemplate, models.EdgeTemplateCreate]):
    """Table operations for edge templates."""


class EdgeOperations(TableOperations[Edge, models.Edge, models.EdgeCreate]):
    """Table operations for provenance graph edges."""


edge_template = EdgeTemplateOperations(TableContext.from_db_class(EdgeTemplate))
edge = EdgeOperations(TableContext.from_db_class(Edge))
