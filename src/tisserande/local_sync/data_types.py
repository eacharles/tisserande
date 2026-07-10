from macon.local_sync.base import SyncOperations

from .. import models
from ..db import data_types as db
from ..local_async import data_types as async_ops


class DataFileTypeSyncOperations(
    SyncOperations[db.DataFileTypeTable, models.DataFileType, models.DataFileTypeCreate],
):
    pass


class ConfigFileTypeSyncOperations(
    SyncOperations[db.ConfigFileTypeTable, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    pass


class ConfigDictTypeSyncOperations(
    SyncOperations[db.ConfigDictTypeTable, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    pass


class ParameterSyncOperations(
    SyncOperations[db.ParameterTable, models.Parameter, models.ParameterCreate],
):
    pass


class ArraySyncOperations(
    SyncOperations[db.ArrayTable, models.Array, models.ArrayCreate],
):
    pass


class ClassSyncOperations(
    SyncOperations[db.ClassTable, models.Class, models.ClassCreate],
):
    pass


data_file_type = DataFileTypeSyncOperations(async_ops.data_file_type)
config_file_type = ConfigFileTypeSyncOperations(async_ops.config_file_type)
config_dict_type = ConfigDictTypeSyncOperations(async_ops.config_dict_type)
parameter = ParameterSyncOperations(async_ops.parameter)
array = ArraySyncOperations(async_ops.array)
class_ = ClassSyncOperations(async_ops.class_)
