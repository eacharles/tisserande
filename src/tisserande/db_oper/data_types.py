from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db import data_types as db


class DataFileTypeOperations(
    TableOperations[db.DataFileType, models.DataFileType, models.DataFileTypeCreate]
):
    """Table operations for data file types."""


class ConfigFileTypeOperations(
    TableOperations[db.ConfigFileType, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    """Table operations for config file types."""


class ConfigDictTypeOperations(
    TableOperations[db.ConfigDictType, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    """Table operations for config dict types."""


class ParameterTypeOperations(
    TableOperations[db.ParameterType, models.ParameterType, models.ParameterTypeCreate],
):
    """Table operations for parameter types."""


class ArrayTypeOperations(
    TableOperations[db.ArrayType, models.ArrayType, models.ArrayTypeCreate],
):
    """Table operations for array types."""


class ClassTypeOperations(TableOperations[db.ClassType, models.Class, models.ClassCreate]):
    """Table operations for Python class types."""


data_file_type = DataFileTypeOperations(TableContext.from_db_class(db.DataFileType))
config_file_type = ConfigFileTypeOperations(TableContext.from_db_class(db.ConfigFileType))
config_dict_type = ConfigDictTypeOperations(TableContext.from_db_class(db.ConfigDictType))
parameter_type = ParameterTypeOperations(TableContext.from_db_class(db.ParameterType))
array_type = ArrayTypeOperations(TableContext.from_db_class(db.ArrayType))
class_type = ClassTypeOperations(TableContext.from_db_class(db.ClassType))
