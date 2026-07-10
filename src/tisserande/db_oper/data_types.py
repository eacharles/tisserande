from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db import data_types as db


class DataFileTypeOperations(
    TableOperations[db.DataFileTypeTable, models.DataFileType, models.DataFileTypeCreate]
):
    """Table operations for data file types."""


class ConfigFileTypeOperations(
    TableOperations[db.ConfigFileTypeTable, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    """Table operations for config file types."""


class ConfigDictTypeOperations(
    TableOperations[db.ConfigDictTypeTable, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    """Table operations for config dict types."""


class ParameterOperations(TableOperations[db.ParameterTable, models.Parameter, models.ParameterCreate]):
    """Table operations for parameters."""


class ArrayOperations(TableOperations[db.ArrayTable, models.Array, models.ArrayCreate]):
    """Table operations for arrays."""


class ClassOperations(TableOperations[db.ClassTable, models.Class, models.ClassCreate]):
    """Table operations for Python classes."""


data_file_type = DataFileTypeOperations(TableContext.from_db_class(db.DataFileTypeTable))
config_file_type = ConfigFileTypeOperations(TableContext.from_db_class(db.ConfigFileTypeTable))
config_dict_type = ConfigDictTypeOperations(TableContext.from_db_class(db.ConfigDictTypeTable))
parameter = ParameterOperations(TableContext.from_db_class(db.ParameterTable))
array = ArrayOperations(TableContext.from_db_class(db.ArrayTable))
class_ = ClassOperations(TableContext.from_db_class(db.ClassTable))
