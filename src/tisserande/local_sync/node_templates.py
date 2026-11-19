from macon.local_sync.base import SyncOperations

from .. import models
from ..db.node_templates import NodeTemplate
from ..local_async.node_templates import node_template as node_template_async


class NodeTemplateSyncOperations(
    SyncOperations[NodeTemplate, models.NodeTemplate, models.NodeTemplateCreate]
):
    """Synchronous operations for node templates."""


node_template = NodeTemplateSyncOperations(node_template_async)
