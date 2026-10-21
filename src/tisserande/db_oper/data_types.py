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


class ParameterOperations(TableOperations[db.Parameter, models.Parameter, models.ParameterCreate]):
    """Table operations for parameters."""


class ArrayOperations(TableOperations[db.Array, models.Array, models.ArrayCreate]):
    """Table operations for arrays."""


class ClassOperations(TableOperations[db.Class, models.Class, models.ClassCreate]):
    """Table operations for Python classes."""


data_file_type = DataFileTypeOperations(TableContext.from_db_class(db.DataFileType))
config_file_type = ConfigFileTypeOperations(TableContext.from_db_class(db.ConfigFileType))
config_dict_type = ConfigDictTypeOperations(TableContext.from_db_class(db.ConfigDictType))
parameter = ParameterOperations(TableContext.from_db_class(db.Parameter))
array = ArrayOperations(TableContext.from_db_class(db.Array))
class_ = ClassOperations(TableContext.from_db_class(db.Class))
