from macon.local_async.base import LocalOperations

from .. import models
from ..db import data_types as db
from ..db_oper import data_types as ops


class DataFileTypeLocalOperations(
    LocalOperations[db.DataFileType, models.DataFileType, models.DataFileTypeCreate],
):
    """Async session-managed operations for data file types."""


class ConfigFileTypeLocalOperations(
    LocalOperations[db.ConfigFileType, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    """Async session-managed operations for config file types."""


class ConfigDictTypeLocalOperations(
    LocalOperations[db.ConfigDictType, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    """Async session-managed operations for config dict types."""


class ParameterTypeLocalOperations(
    LocalOperations[db.ParameterType, models.ParameterType, models.ParameterTypeCreate],
):
    """Async session-managed operations for parameter types."""


class ArrayTypeLocalOperations(
    LocalOperations[db.ArrayType, models.ArrayType, models.ArrayTypeCreate],
):
    """Async session-managed operations for array types."""


class ClassTypeLocalOperations(
    LocalOperations[db.ClassType, models.Class, models.ClassCreate],
):
    """Async session-managed operations for Python class types."""


data_file_type = DataFileTypeLocalOperations(ops.data_file_type)
config_file_type = ConfigFileTypeLocalOperations(ops.config_file_type)
config_dict_type = ConfigDictTypeLocalOperations(ops.config_dict_type)
parameter_type = ParameterTypeLocalOperations(ops.parameter_type)
array_type = ArrayTypeLocalOperations(ops.array_type)
class_type = ClassTypeLocalOperations(ops.class_type)
