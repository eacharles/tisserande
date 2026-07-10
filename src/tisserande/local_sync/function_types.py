from macon.local_sync.base import SyncOperations

from .. import models
from ..db import function_types as db
from ..local_async import function_types as async_ops


class PythonFunctionSyncOperations(
    SyncOperations[db.PythonFunctionTable, models.PythonFunction, models.PythonFunctionCreate],
):
    """Synchronous operations for Python functions."""


class MemberFunctionSyncOperations(
    SyncOperations[db.MemberFunctionTable, models.MemberFunction, models.MemberFunctionCreate],
):
    """Synchronous operations for member functions."""


class ShellFunctionSyncOperations(
    SyncOperations[db.ShellFunctionTable, models.ShellFunction, models.ShellFunctionCreate],
):
    """Synchronous operations for shell functions."""


python_function = PythonFunctionSyncOperations(async_ops.python_function)
member_function = MemberFunctionSyncOperations(async_ops.member_function)
shell_function = ShellFunctionSyncOperations(async_ops.shell_function)
