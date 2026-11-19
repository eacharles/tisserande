from macon.local_sync.base import SyncOperations

from .. import models
from ..db.associations import AssocTemplate, Association
from ..local_async.associations import assoc_template as assoc_template_async
from ..local_async.associations import association as association_async


class AssocTemplateSyncOperations(SyncOperations[AssocTemplate, models.AssocTemplate, models.AssocTemplateCreate]):
    """Synchronous operations for assoc templates."""


class AssociationSyncOperations(SyncOperations[Association, models.Association, models.AssociationCreate]):
    """Synchronous operations for node–graph associations."""


assoc_template = AssocTemplateSyncOperations(assoc_template_async)
association = AssociationSyncOperations(association_async)
