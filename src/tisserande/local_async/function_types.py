from macon.local_async.base import LocalOperations

from .. import models
from ..db import function_types as db
from ..db_oper import function_types as ops


class PythonFunctionLocalOperations(
    LocalOperations[db.PythonFunctionTable, models.PythonFunction, models.PythonFunctionCreate],
):
    pass


class MemberFunctionLocalOperations(
    LocalOperations[db.MemberFunctionTable, models.MemberFunction, models.MemberFunctionCreate],
):
    pass


class ShellFunctionLocalOperations(
    LocalOperations[db.ShellFunctionTable, models.ShellFunction, models.ShellFunctionCreate],
):
    pass


python_function = PythonFunctionLocalOperations(ops.python_function)
member_function = MemberFunctionLocalOperations(ops.member_function)
shell_function = ShellFunctionLocalOperations(ops.shell_function)
