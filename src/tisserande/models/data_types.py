"""Pydantic models for data-related type tables (DataFileType, ConfigFileType, etc.)."""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class DataFileTypeBase(BaseModel):
    """Model for a type of file that contains data."""

    name: str = Field(..., description="Name of the data file type")


class DataFileTypeCreate(DataFileTypeBase):
    """Fields used to create a DataFileType."""


class DataFileType(DataFileTypeBase):
    """DataFileType response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0)


class ConfigFileTypeBase(BaseModel):
    """Model for a type of file that contains configuration."""

    name: str = Field(..., description="Name of the config file type")


class ConfigFileTypeCreate(ConfigFileTypeBase):
    """Fields used to create a ConfigFileType."""


class ConfigFileType(ConfigFileTypeBase):
    """ConfigFileType response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0)


class ConfigDictTypeBase(BaseModel):
    """Model for a type of dict that contains configuration."""

    name: str = Field(..., description="Name of the config dict type")


class ConfigDictTypeCreate(ConfigDictTypeBase):
    """Fields used to create a ConfigDictType."""


class ConfigDictType(ConfigDictTypeBase):
    """ConfigDictType response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0)


class ParameterBase(BaseModel):
    """Model for a parameter definition."""

    name: str = Field(..., description="Name of the parameter")


class ParameterCreate(ParameterBase):
    """Fields used to create a Parameter."""


class Parameter(ParameterBase):
    """Parameter response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0)


class ArrayBase(BaseModel):
    """Model for an array definition."""

    name: str = Field(..., description="Name of the array")
    n_dim: int = Field(..., description="Number of dimensions")
    shape: list[int] = Field(..., description="Shape of the array")


class ArrayCreate(ArrayBase):
    """Fields used to create an Array."""


class Array(ArrayBase):
    """Array response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "n_dim", "shape"]

    id_: int = Field(..., gt=0)


class ClassBase(BaseModel):
    """Model for a Python class definition."""

    name: str = Field(..., description="Name of the class")
    module_: str = Field(..., description="Python module where it lives")


class ClassCreate(ClassBase):
    """Fields used to create a Class."""


class Class(ClassBase):
    """Class response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "module_"]

    id_: int = Field(..., gt=0)
