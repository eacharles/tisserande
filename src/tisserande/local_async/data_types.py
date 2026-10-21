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


class ParameterLocalOperations(
    LocalOperations[db.Parameter, models.Parameter, models.ParameterCreate],
):
    """Async session-managed operations for parameters."""


class ArrayLocalOperations(
    LocalOperations[db.Array, models.Array, models.ArrayCreate],
):
    """Async session-managed operations for arrays."""


class ClassLocalOperations(
    LocalOperations[db.Class, models.Class, models.ClassCreate],
):
    """Async session-managed operations for classes."""


data_file_type = DataFileTypeLocalOperations(ops.data_file_type)
config_file_type = ConfigFileTypeLocalOperations(ops.config_file_type)
config_dict_type = ConfigDictTypeLocalOperations(ops.config_dict_type)
parameter = ParameterLocalOperations(ops.parameter)
array = ArrayLocalOperations(ops.array)
class_ = ClassLocalOperations(ops.class_)
