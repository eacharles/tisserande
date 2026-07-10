from typing import Any

from macon.db_oper.base import TableContext, TableOperations
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models
from ..db.execution import ExecutionTable
from ..models.types import ExecutionStatus


class ExecutionOperations(TableOperations[ExecutionTable, models.Execution, models.ExecutionCreate]):
    """Table operations for executions with status enum conversion."""

    async def get_create_kwargs(
        self,
        session: AsyncSession,
        **kwargs: Any,
    ) -> dict[str, Any]:
        status = kwargs.get("status")
        if isinstance(status, ExecutionStatus):
            kwargs["status"] = status.value
        return kwargs


execution = ExecutionOperations(TableContext.from_db_class(ExecutionTable))
