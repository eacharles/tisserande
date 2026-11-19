from macon.local_async.base import LocalOperations

from .. import models
from ..db.node_templates import NodeTemplate
from ..db_oper.node_templates import node_template as node_template_ops


class NodeTemplateLocalOperations(
    LocalOperations[NodeTemplate, models.NodeTemplate, models.NodeTemplateCreate]
):
    """Async session-managed operations for node templates."""


node_template = NodeTemplateLocalOperations(node_template_ops)
