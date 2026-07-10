Type Annotations
================

Tisserande uses Python's ``typing.Annotated`` to let you explicitly declare
how function arguments should be classified in the provenance graph.

Available Annotations
---------------------

Import from ``tisserande.tracking.annotations``:

.. list-table::
   :header-rows: 1
   :widths: 20 30 50

   * - Annotation
     - Node Type
     - Description
   * - ``DataFile[T]``
     - ``data_file``
     - Path to a data file (FITS, HDF5, Parquet, CSV, etc.)
   * - ``ConfigFile[T]``
     - ``config_file``
     - Path to a configuration file (YAML, JSON, TOML, INI)
   * - ``ConfigDict[T]``
     - ``config_dict``
     - Dictionary containing configuration data
   * - ``Param[T]``
     - ``parameter``
     - Numeric parameter value
   * - ``ArrayArg[T]``
     - ``array``
     - Array of numeric values
   * - ``ObjectArg[T]``
     - ``object``
     - Arbitrary Python object
   * - ``Untracked[T]``
     - *(skipped)*
     - Argument will not be recorded in the provenance graph

Usage
-----

.. code-block:: python

   from tisserande.tracking import track
   from tisserande.tracking.annotations import (
       DataFile, ConfigFile, ConfigDict, Param, Untracked,
   )

   @track
   def photometric_redshift(
       catalog: DataFile[str],
       config: ConfigFile[str],
       settings: ConfigDict[dict],
       n_neighbors: Param[int],
       verbose: Untracked[bool] = False,
   ) -> DataFile[str]:
       # catalog → tracked as data_file node
       # config → tracked as config_file node
       # settings → tracked as config_dict node (full dict stored)
       # n_neighbors → tracked as parameter node (value stored)
       # verbose → NOT tracked (marked Untracked)
       ...
       return "/data/results/photo_z.fits"  # tracked as data_file output

How It Works
------------

The annotations use Python's ``typing.Annotated`` with string metadata:

.. code-block:: python

   DataFile = Annotated[T, "tisserande:data_file"]
   Param = Annotated[T, "tisserande:parameter"]
   Untracked = Annotated[T, "tisserande:untracked"]

The ``ArgumentInspector`` reads type hints via ``typing.get_type_hints()``
(with ``include_extras=True``) and extracts the tisserande metadata to
determine the node type.

Automatic Classification (Heuristics)
--------------------------------------

If no annotation is provided, tisserande uses heuristics based on the
runtime value:

.. list-table::
   :header-rows: 1
   :widths: 40 30

   * - Value Pattern
     - Classified As
   * - ``int`` or ``float``
     - ``parameter``
   * - ``str`` with path separator or data extension (``.fits``, ``.hdf5``, etc.)
     - ``data_file``
   * - ``str`` with config extension (``.yaml``, ``.json``, ``.toml``, etc.)
     - ``config_file``
   * - ``dict``
     - ``config_dict``
   * - ``list``/``tuple`` of numbers
     - ``array``
   * - Everything else
     - ``object``

These heuristics provide reasonable defaults, but explicit annotations are
recommended for clarity and correctness.

Return Value Classification
---------------------------

Return values follow the same rules:

- If the function has a return type annotation with tisserande metadata, that's used
- Otherwise, heuristics are applied to the actual return value
- Tuple returns create multiple output nodes (one per element)

.. code-block:: python

   @track
   def split_data(catalog: DataFile[str]) -> tuple[DataFile[str], DataFile[str]]:
       # Returns create two output data_file nodes
       return "/data/train.fits", "/data/test.fits"
