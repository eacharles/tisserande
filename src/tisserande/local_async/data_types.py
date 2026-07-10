from macon.local_async.base import LocalOperations

from .. import models
from ..db import data_types as db
from ..db_oper import data_types as ops


class DataFileTypeLocalOperations(
    LocalOperations[db.DataFileTypeTable, models.DataFileType, models.DataFileTypeCreate],
):
    pass


class ConfigFileTypeLocalOperations(
    LocalOperations[db.ConfigFileTypeTable, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    pass


class ConfigDictTypeLocalOperations(
    LocalOperations[db.ConfigDictTypeTable, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    pass


class ParameterLocalOperations(
    LocalOperations[db.ParameterTable, models.Parameter, models.ParameterCreate],
):
    pass


class ArrayLocalOperations(
    LocalOperations[db.ArrayTable, models.Array, models.ArrayCreate],
):
    pass


class ClassLocalOperations(
    LocalOperations[db.ClassTable, models.Class, models.ClassCreate],
):
    pass


data_file_type = DataFileTypeLocalOperations(ops.data_file_type)
config_file_type = ConfigFileTypeLocalOperations(ops.config_file_type)
config_dict_type = ConfigDictTypeLocalOperations(ops.config_dict_type)
parameter = ParameterLocalOperations(ops.parameter)
array = ArrayLocalOperations(ops.array)
class_ = ClassLocalOperations(ops.class_)
