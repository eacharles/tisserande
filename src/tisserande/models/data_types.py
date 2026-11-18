"""Pydantic models for data-related type tables (DataFileType, ConfigFileType, etc.)."""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


# DataFile

class DataFileTypeMixin:
    """Mixin class for a DataNodeTemplate that is a data file."""


class DataFileTypeCreate(DataNodeTemplateCreate, DataFileTypeMixin):
    """Fields used to create a DataFileType that are not in the DB."""


class DataFileType(DataNodeTemplate, DataFileTypeMixin):
    """DataFileType response model."""


class DataFileMixin:
    """Mixin class for a DataNode that is a data file."""


class DataFileCreate(DataNodeCreate, DataFileMixin):
    """Fields used to create a DataFile that are not in the DB."""


class DataFile(DataNodeTemplate, DataFileMixin)
    """DataFile response model."""



# ConfigFile

class ConfigFileTypeMixin:
    """Mixin class for a DataNodeTemplate that is a configuration file."""


class ConfigFileTypeCreate(DataNodeTemplateCreate, ConfigFileTypeMixin):
    """Fields used to create a ConfigFileType that are not in the DB."""


class ConfigFileType(DataNodeTemplate, ConfigFileTypeMixin):
    """ConfigFileType response model."""


class ConfigFileMixin:
    """Mixin class for a DataNode that is a configuration file."""


class ConfigFileCreate(DataNodeCreate, ConfigFileMixin):
    """Fields used to create a ConfigFile that are not in the DB."""


class ConfigFile(DataNode, ConfigFileMixin):
    """ConfigFile response model."""


# ConfigDict

class ConfigDictTypeMixin:
    """Mixin class for a DataNodeTemplate that is a configuraiton dict."""


class ConfigDictTypeCreate(DataNodeTemplateCreate, ConfigDictTypeMixin):
    """Fields used to create a ConfigDictType that are not in the DB."""


class ConfigDictType(DataNodeTemplate, ConfigDictTypeMixin):
    """ConfigDictType response model."""


class ConfigDictMixin:
    """Mixin class for a DataNode that is a configuraiton dict."""


class ConfigDictCreate(DataNodeCreate, ConfigDictMixin):
    """Fields used to create a ConfigDict that are not in the DB."""


class ConfigDict(DataNode, ConfigDictMixin):
    """ConfigDict response model."""


# Parameter

class ParameterTypeMixin:
    """Mixin class for a DataNodeTemplate that is simple parameter."""


class ParameterTypeCreate(DataNodeTemplateCreate, ParameterTypeMixin):
    """Includes fields used to create a ParameterType that are not in the DB."""


class ParameterType(DataNodeTemplate, ParameterTypeMixin):
    """Parameter response model."""


class ParameterMixin:
    """Mixin class for a DataNode that is simple parameter."""


class ParameterCreate(DataNodeCreate, ParameterMixin):
    """Includes fields used to create a Parameter that are not in the DB."""


class Parameter(DataNode, ParameterMixin):
    """Parameter response model."""


# Array

class ArrayTypeMixin:
    """Mixin class for a DataNodeTemplate that is an array."""


class ArrayTypeCreate(DataNodeTemplateCreate, ArrayTypeMixin):
    """Includes fields used to create a ArrayType that are not in the DB."""


class ArrayType(DataNodeTemplateCreate, ArrayTypeMixin):
    """ArrayType response model."""


class ArrayMixin:
    """Mixin class for a DataNode that is an array."""


class ArrayCreate(DataNodeCreate, ArrayMixin):
    """Includes fields used to create an Array that are not in the DB."""


class Array(DataNodeCreate, ArrayMixin):
    """Array response model."""


# Class

class ClassMixin:
    """Mixin class for a DataNodeTemplate that is a python class."""


class ClassCreate(DataNodeTemplateCreate, ClassMixin):
    """Includes fields used to create a Class that are not in the DB."""


class Class(DataNodeTemplate, ClassMixin):
    """Class response model."""


class ClassInstanceMixin:
    """Mixin class for a DataNode that is a python class."""


class ClassInstanceCreate(DataNodeCreate, ClassInstanceMixin):
    """Includes fields used to create a ClassInstance that are not in the DB."""


class ClassInstance(DataNode, ClassInstanceMixin):
    """ClassInstance response model."""
