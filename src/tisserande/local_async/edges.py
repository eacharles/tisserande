from macon.local_async.base import LocalOperations

from .. import models
from ..db.edges import EdgeTable
from ..db_oper.edges import edge as edge_ops


class EdgeLocalOperations(LocalOperations[EdgeTable, models.Edge, models.EdgeCreate]):
    """Async session-managed operations for edges."""


edge = EdgeLocalOperations(edge_ops)
