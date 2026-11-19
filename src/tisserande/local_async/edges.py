from macon.local_async.base import LocalOperations

from .. import models
from ..db.edges import Edge, EdgeTemplate
from ..db_oper.edges import edge as edge_ops
from ..db_oper.edges import edge_template as edge_template_ops


class EdgeTemplateLocalOperations(
    LocalOperations[EdgeTemplate, models.EdgeTemplate, models.EdgeTemplateCreate]
):
    """Async session-managed operations for edge templates."""


class EdgeLocalOperations(LocalOperations[Edge, models.Edge, models.EdgeCreate]):
    """Async session-managed operations for edges."""


edge_template = EdgeTemplateLocalOperations(edge_template_ops)
edge = EdgeLocalOperations(edge_ops)
