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


class ParameterSyncOperations(
    SyncOperations[db.Parameter, models.Parameter, models.ParameterCreate],
):
    """Synchronous operations for parameters."""


class ArraySyncOperations(
    SyncOperations[db.Array, models.Array, models.ArrayCreate],
):
    """Synchronous operations for arrays."""


class ClassSyncOperations(
    SyncOperations[db.Class, models.Class, models.ClassCreate],
):
    """Synchronous operations for classes."""


data_file_type = DataFileTypeSyncOperations(async_ops.data_file_type)
config_file_type = ConfigFileTypeSyncOperations(async_ops.config_file_type)
config_dict_type = ConfigDictTypeSyncOperations(async_ops.config_dict_type)
parameter = ParameterSyncOperations(async_ops.parameter)
array = ArraySyncOperations(async_ops.array)
class_ = ClassSyncOperations(async_ops.class_)
