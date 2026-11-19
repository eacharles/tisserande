from macon.local_async.base import LocalOperations

from .. import models
from ..db.associations import AssocTemplate, Association
from ..db_oper.associations import assoc_template as assoc_template_ops
from ..db_oper.associations import association as association_ops


class AssocTemplateLocalOperations(LocalOperations[AssocTemplate, models.AssocTemplate, models.AssocTemplateCreate]):
    """Async session-managed operations for assoc templates."""


class AssociationLocalOperations(LocalOperations[Association, models.Association, models.AssociationCreate]):
    """Async session-managed operations for node–graph associations."""


assoc_template = AssocTemplateLocalOperations(assoc_template_ops)
association = AssociationLocalOperations(association_ops)
