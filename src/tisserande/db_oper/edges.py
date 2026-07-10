from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.edges import EdgeTable


class EdgeOperations(TableOperations[EdgeTable, models.Edge, models.EdgeCreate]):
    pass


edge = EdgeOperations(TableContext.from_db_class(EdgeTable))
