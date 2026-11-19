"""Pydantic models for data-type node templates and their runtime instances.

Each data type is represented by two parallel sets of models:

* A *Template* pair (``...TypeCreate`` / ``...Type`` or ``...Create`` / ``...``
  for Class) — reusable type definitions stored once in the NodeTemplate table.
* An *Instance* pair (``...Create`` / ``...``) — runtime node records stored
  in the Node table, each optionally referencing a template.

Both sets follow the ``Base → Create → Response`` pattern established in
``base.py`` and use a plain mixin class to supply type-specific fields and
lock the ``node_template_type`` / ``node_type`` discriminator to a ``Literal``.
"""

from typing import Any, Literal

from pydantic import Field

from .base import (
    DataNode,
    DataNodeCreate,
    DataNodeTemplate,
    DataNodeTemplateCreate,
)
from .types import NodeTemplateType, NodeType


# ---------------------------------------------------------------------------
# DataFile
# ---------------------------------------------------------------------------


class DataFileTypeMixin:
    """Mixin for a DataNodeTemplate that represents a data file type.

    ``file_format`` records the expected file format for all files of this
    type (e.g. ``"FITS"``, ``"HDF5"``, ``"parquet"``), enabling format-aware
    queries across the provenance graph without inspecting individual file
    paths.
    """

    node_template_type: Literal[NodeTemplateType.DATA_FILE_TYPE] = NodeTemplateType.DATA_FILE_TYPE
    file_format: str | None = Field(default=None, description="Expected file format for this type (e.g. 'FITS', 'HDF5', 'parquet').")


class DataFileTypeCreate(DataNodeTemplateCreate, DataFileTypeMixin):
    """Creation model for a DataFileType template."""


class DataFileType(DataNodeTemplate, DataFileTypeMixin):
    """Response model for a DataFileType template."""


class DataFileMixin:
    """Mixin for a DataNode that is a specific data file.

    ``file_hash`` and ``hash_algorithm`` together provide an integrity
    fingerprint so downstream consumers can verify they are reading exactly
    the file that was recorded.  ``file_size_bytes`` gives a quick sanity
    check without opening the file.
    """

    node_type: Literal[NodeType.DATA_FILE] = NodeType.DATA_FILE
    file_path: str = Field(..., description="Path to the data file.")
    file_hash: str | None = Field(default=None, description="Hex-encoded checksum of the file contents.")
    hash_algorithm: str | None = Field(default=None, description="Algorithm used to compute file_hash (e.g. 'sha256', 'md5').")
    file_size_bytes: int | None = Field(default=None, description="File size in bytes.")


class DataFileCreate(DataNodeCreate, DataFileMixin):
    """Creation model for a DataFile node."""


class DataFile(DataNode, DataFileMixin):
    """Response model for a DataFile node."""


# ---------------------------------------------------------------------------
# ConfigFile
# ---------------------------------------------------------------------------


class ConfigFileTypeMixin:
    """Mixin for a DataNodeTemplate that represents a configuration file type."""

    node_template_type: Literal[NodeTemplateType.CONFIG_FILE_TYPE] = NodeTemplateType.CONFIG_FILE_TYPE


class ConfigFileTypeCreate(DataNodeTemplateCreate, ConfigFileTypeMixin):
    """Creation model for a ConfigFileType template."""


class ConfigFileType(DataNodeTemplate, ConfigFileTypeMixin):
    """Response model for a ConfigFileType template."""


class ConfigFileMixin:
    """Mixin for a DataNode that is a specific configuration file.

    ``file_hash`` and ``hash_algorithm`` serve the same integrity purpose as
    on ``DataFileMixin``: they let the provenance system detect if a config
    file changed between runs.
    """

    node_type: Literal[NodeType.CONFIG_FILE] = NodeType.CONFIG_FILE
    file_path: str = Field(..., description="Path to the configuration file.")
    file_hash: str | None = Field(default=None, description="Hex-encoded checksum of the file contents.")
    hash_algorithm: str | None = Field(default=None, description="Algorithm used to compute file_hash (e.g. 'sha256', 'md5').")
    file_size_bytes: int | None = Field(default=None, description="File size in bytes.")


class ConfigFileCreate(DataNodeCreate, ConfigFileMixin):
    """Creation model for a ConfigFile node."""


class ConfigFile(DataNode, ConfigFileMixin):
    """Response model for a ConfigFile node."""


# ---------------------------------------------------------------------------
# ConfigDict
# ---------------------------------------------------------------------------


class ConfigDictTypeMixin:
    """Mixin for a DataNodeTemplate that represents a configuration dictionary type.

    ``default_config`` captures the default values associated with this type of
    configuration, stored once at the template level.
    """

    node_template_type: Literal[NodeTemplateType.CONFIG_DICT_TYPE] = NodeTemplateType.CONFIG_DICT_TYPE
    default_config: dict[str, Any] = Field(..., description="Default configuration values for this template.")


class ConfigDictTypeCreate(DataNodeTemplateCreate, ConfigDictTypeMixin):
    """Creation model for a ConfigDictType template."""


class ConfigDictType(DataNodeTemplate, ConfigDictTypeMixin):
    """Response model for a ConfigDictType template."""


class ConfigDictMixin:
    """Mixin for a DataNode that holds a specific configuration dictionary."""

    node_type: Literal[NodeType.CONFIG_DICT] = NodeType.CONFIG_DICT
    config_data: dict[str, Any] = Field(..., description="Configuration data for this specific node.")


class ConfigDictCreate(DataNodeCreate, ConfigDictMixin):
    """Creation model for a ConfigDict node."""


class ConfigDict(DataNode, ConfigDictMixin):
    """Response model for a ConfigDict node."""


# ---------------------------------------------------------------------------
# Parameter
# ---------------------------------------------------------------------------


class ParameterTypeMixin:
    """Mixin for a DataNodeTemplate that represents a named scalar parameter type.

    ``units`` records the physical units expected for all parameters of this
    type (e.g. ``"deg"``, ``"Mpc/h"``).  ``dtype`` constrains the value type
    (``"float"``, ``"int"``, ``"str"``).  Both are stored on the template so
    they do not need to be repeated on every individual parameter node.
    """

    node_template_type: Literal[NodeTemplateType.PARAMETER_TYPE] = NodeTemplateType.PARAMETER_TYPE
    units: str | None = Field(default=None, description="Physical units expected for this parameter type (e.g. 'deg', 'Mpc/h', 'eV').")
    dtype: str | None = Field(default=None, description="Expected value type: 'float', 'int', or 'str'.")


class ParameterTypeCreate(DataNodeTemplateCreate, ParameterTypeMixin):
    """Creation model for a ParameterType template."""


class ParameterType(DataNodeTemplate, ParameterTypeMixin):
    """Response model for a ParameterType template."""


class ParameterMixin:
    """Mixin for a DataNode that holds a scalar numeric parameter value.

    ``units`` on the instance may differ from the template default when a
    caller supplies a value in a compatible but different unit system.
    """

    node_type: Literal[NodeType.PARAMETER] = NodeType.PARAMETER
    value: float = Field(..., description="Numeric value of this parameter.")
    units: str | None = Field(default=None, description="Physical units of this parameter value. Overrides the template default when set.")


class ParameterCreate(DataNodeCreate, ParameterMixin):
    """Creation model for a Parameter node."""


class Parameter(DataNode, ParameterMixin):
    """Response model for a Parameter node."""


# ---------------------------------------------------------------------------
# Array
# ---------------------------------------------------------------------------


class ArrayTypeMixin:
    """Mixin for a DataNodeTemplate that represents an array type.

    ``dtype`` records the expected numpy dtype string (e.g. ``"float64"``).
    ``units`` records the physical units on the array values.  ``ndim``
    constrains the expected number of dimensions, enabling shape validation
    at the graph-template level before any data is produced.
    """

    node_template_type: Literal[NodeTemplateType.ARRAY_TYPE] = NodeTemplateType.ARRAY_TYPE
    dtype: str | None = Field(default=None, description="Expected numpy dtype string (e.g. 'float64', 'int32').")
    units: str | None = Field(default=None, description="Physical units on the array values (e.g. 'deg', 'Jy').")
    ndim: int | None = Field(default=None, description="Expected number of dimensions.")


class ArrayTypeCreate(DataNodeTemplateCreate, ArrayTypeMixin):
    """Creation model for an ArrayType template."""


class ArrayType(DataNodeTemplate, ArrayTypeMixin):
    """Response model for an ArrayType template."""


class ArrayMixin:
    """Mixin for a DataNode that holds an array.

    ``shape`` records the actual array dimensions.  ``dtype`` records the
    actual numpy dtype of this specific array instance.  ``value_json``
    optionally stores a JSON-serialisable representation of the contents for
    small arrays; large arrays are typically referenced via ``file_path``
    instead, which points to the backing file (e.g. a FITS or HDF5 file).
    """

    node_type: Literal[NodeType.ARRAY] = NodeType.ARRAY
    shape: list[int] = Field(..., description="Shape of the array (list of dimension sizes).")
    dtype: str | None = Field(default=None, description="Numpy dtype string of this array instance (e.g. 'float64').")
    file_path: str | None = Field(default=None, description="Path to the file storing this array when it is too large to serialise inline.")
    value_json: Any | None = Field(default=None, description="Optional JSON-serialisable representation of small array contents.")


class ArrayCreate(DataNodeCreate, ArrayMixin):
    """Creation model for an Array node."""


class Array(DataNode, ArrayMixin):
    """Response model for an Array node."""


# ---------------------------------------------------------------------------
# Class (Python class type template) and ClassInstance
# ---------------------------------------------------------------------------


class ClassMixin:
    """Mixin for a DataNodeTemplate that describes a Python class.

    ``module_`` identifies where the class lives so it can be imported
    programmatically.  The trailing underscore avoids shadowing the Python
    built-in ``module``.  Together with ``name`` from the base template, the
    fully-qualified class name is ``module_ + "." + name``.
    """

    node_template_type: Literal[NodeTemplateType.CLASS_TYPE] = NodeTemplateType.CLASS_TYPE
    module_: str = Field(..., description="Fully-qualified module where this class is defined (e.g. 'mypackage.models').")


class ClassCreate(DataNodeTemplateCreate, ClassMixin):
    """Creation model for a Class template."""


class Class(DataNodeTemplate, ClassMixin):
    """Response model for a Class template."""


class ClassInstanceMixin:
    """Mixin for a DataNode that is a specific instance of a Python class.

    ``ctor_values_json`` optionally captures the constructor arguments used to
    create this instance in a JSON-serialisable form, enabling reproduction of
    the same object state from the provenance record alone.
    """

    node_type: Literal[NodeType.CLASS_INSTANCE] = NodeType.CLASS_INSTANCE
    ctor_values_json: Any | None = Field(default=None, description="Optional JSON-serialisable constructor arguments used to create this instance.")


class ClassInstanceCreate(DataNodeCreate, ClassInstanceMixin):
    """Creation model for a ClassInstance node."""


class ClassInstance(DataNode, ClassInstanceMixin):
    """Response model for a ClassInstance node."""
