from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.node_templates import NodeTemplate


class NodeTemplateOperations(TableOperations[NodeTemplate, models.NodeTemplate, models.NodeTemplateCreate]):
    """Table operations for the NodeTemplate base table."""


node_template = NodeTemplateOperations(TableContext.from_db_class(NodeTemplate))
