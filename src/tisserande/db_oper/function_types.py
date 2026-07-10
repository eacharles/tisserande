from typing import Any

from macon import db_funcs
from macon.common import RowId
from macon.db_oper.base import TableContext, TableOperations
from sqlalchemy.ext.asyncio import AsyncSession

from .. import models
from ..db import data_types as db_data
from ..db import function_types as db


class PythonFunctionOperations(
    TableOperations[db.PythonFunctionTable, models.PythonFunction, models.PythonFunctionCreate],
):
    """Table operations for Python functions."""


class MemberFunctionOperations(
    TableOperations[db.MemberFunctionTable, models.MemberFunction, models.MemberFunctionCreate],
):
    """Table operations for member functions with class FK resolution."""

    async def get_create_kwargs(
        self,
        session: AsyncSession,
        class_id: RowId | None = None,
        class_name: str | None = None,
        **kwargs: Any,
    ) -> dict[str, Any]:
        class_id, _ = await db_funcs.read.lookup_by_id_or_name(
            db_data.ClassTable,
            session,
            class_id,
            class_name,
        )
        return {"class_id": class_id, **kwargs}


class ShellFunctionOperations(
    TableOperations[db.ShellFunctionTable, models.ShellFunction, models.ShellFunctionCreate],
):
    """Table operations for shell functions."""


python_function = PythonFunctionOperations(TableContext.from_db_class(db.PythonFunctionTable))
member_function = MemberFunctionOperations(TableContext.from_db_class(db.MemberFunctionTable))
shell_function = ShellFunctionOperations(TableContext.from_db_class(db.ShellFunctionTable))
