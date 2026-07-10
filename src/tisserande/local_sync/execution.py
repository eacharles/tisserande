from macon.local_sync.base import SyncOperations

from .. import models
from ..db.execution import ExecutionTable
from ..local_async.execution import execution as execution_async


class ExecutionSyncOperations(SyncOperations[ExecutionTable, models.Execution, models.ExecutionCreate]):
    """Synchronous operations for executions."""


execution = ExecutionSyncOperations(execution_async)
