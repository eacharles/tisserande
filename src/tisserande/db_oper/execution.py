from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db.execution import ExecutionTable


class ExecutionOperations(TableOperations[ExecutionTable, models.Execution, models.ExecutionCreate]):
    pass


execution = ExecutionOperations(TableContext.from_db_class(ExecutionTable))
