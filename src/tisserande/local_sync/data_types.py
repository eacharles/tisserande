from macon.local_sync.base import SyncOperations

from .. import models
from ..db import data_types as db
from ..local_async import data_types as async_ops


class DataFileTypeSyncOperations(
    SyncOperations[db.DataFileType, models.DataFileType, models.DataFileTypeCreate],
):
    """Synchronous operations for data file types."""


class ConfigFileTypeSyncOperations(
    SyncOperations[db.ConfigFileType, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    """Synchronous operations for config file types."""


class ConfigDictTypeSyncOperations(
    SyncOperations[db.ConfigDictType, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    """Synchronous operations for config dict types."""


class ParameterTypeSyncOperations(
    SyncOperations[db.ParameterType, models.ParameterType, models.ParameterTypeCreate],
):
    """Synchronous operations for parameter types."""


class ArrayTypeSyncOperations(
    SyncOperations[db.ArrayType, models.ArrayType, models.ArrayTypeCreate],
):
    """Synchronous operations for array types."""


class ClassTypeSyncOperations(
    SyncOperations[db.ClassType, models.Class, models.ClassCreate],
):
    """Synchronous operations for Python class types."""


data_file_type = DataFileTypeSyncOperations(async_ops.data_file_type)
config_file_type = ConfigFileTypeSyncOperations(async_ops.config_file_type)
config_dict_type = ConfigDictTypeSyncOperations(async_ops.config_dict_type)
parameter_type = ParameterTypeSyncOperations(async_ops.parameter_type)
array_type = ArrayTypeSyncOperations(async_ops.array_type)
class_type = ClassTypeSyncOperations(async_ops.class_type)
