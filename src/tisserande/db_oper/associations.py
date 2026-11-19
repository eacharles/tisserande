from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.associations import AssocTemplate, Association


class AssocTemplateOperations(
    TableOperations[AssocTemplate, models.AssocTemplate, models.AssocTemplateCreate]
):
    """Table operations for assoc templates."""


class AssociationOperations(TableOperations[Association, models.Association, models.AssociationCreate]):
    """Table operations for node–graph associations."""


assoc_template = AssocTemplateOperations(TableContext.from_db_class(AssocTemplate))
association = AssociationOperations(TableContext.from_db_class(Association))
