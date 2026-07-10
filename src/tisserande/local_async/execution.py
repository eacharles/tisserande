from macon.local_async.base import LocalOperations

from .. import models
from ..db.execution import ExecutionTable
from ..db_oper.execution import execution as execution_ops


class ExecutionLocalOperations(LocalOperations[ExecutionTable, models.Execution, models.ExecutionCreate]):
    pass


execution = ExecutionLocalOperations(execution_ops)
