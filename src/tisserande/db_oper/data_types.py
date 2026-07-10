from macon.db_oper.base import TableContext, TableOperations

from .. import models
from ..db import data_types as db


class DataFileTypeOperations(
    TableOperations[db.DataFileTypeTable, models.DataFileType, models.DataFileTypeCreate]
):
    pass


class ConfigFileTypeOperations(
    TableOperations[db.ConfigFileTypeTable, models.ConfigFileType, models.ConfigFileTypeCreate],
):
    pass


class ConfigDictTypeOperations(
    TableOperations[db.ConfigDictTypeTable, models.ConfigDictType, models.ConfigDictTypeCreate],
):
    pass


class ParameterOperations(TableOperations[db.ParameterTable, models.Parameter, models.ParameterCreate]):
    pass


class ArrayOperations(TableOperations[db.ArrayTable, models.Array, models.ArrayCreate]):
    pass


class ClassOperations(TableOperations[db.ClassTable, models.Class, models.ClassCreate]):
    pass


data_file_type = DataFileTypeOperations(TableContext.from_db_class(db.DataFileTypeTable))
config_file_type = ConfigFileTypeOperations(TableContext.from_db_class(db.ConfigFileTypeTable))
config_dict_type = ConfigDictTypeOperations(TableContext.from_db_class(db.ConfigDictTypeTable))
parameter = ParameterOperations(TableContext.from_db_class(db.ParameterTable))
array = ArrayOperations(TableContext.from_db_class(db.ArrayTable))
class_ = ClassOperations(TableContext.from_db_class(db.ClassTable))
