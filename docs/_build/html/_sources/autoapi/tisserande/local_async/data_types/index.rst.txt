tisserande.local_async.data_types
=================================

.. py:module:: tisserande.local_async.data_types


Attributes
----------

.. autoapisummary::

   tisserande.local_async.data_types.data_file_type
   tisserande.local_async.data_types.config_file_type
   tisserande.local_async.data_types.config_dict_type
   tisserande.local_async.data_types.parameter
   tisserande.local_async.data_types.array
   tisserande.local_async.data_types.class_


Classes
-------

.. autoapisummary::

   tisserande.local_async.data_types.DataFileTypeLocalOperations
   tisserande.local_async.data_types.ConfigFileTypeLocalOperations
   tisserande.local_async.data_types.ConfigDictTypeLocalOperations
   tisserande.local_async.data_types.ParameterLocalOperations
   tisserande.local_async.data_types.ArrayLocalOperations
   tisserande.local_async.data_types.ClassLocalOperations


Module Contents
---------------

.. py:class:: DataFileTypeLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.DataFileTypeTable`\ , :py:obj:`tisserande.models.DataFileType`\ , :py:obj:`tisserande.models.DataFileTypeCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ConfigFileTypeLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigFileTypeTable`\ , :py:obj:`tisserande.models.ConfigFileType`\ , :py:obj:`tisserande.models.ConfigFileTypeCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ConfigDictTypeLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigDictTypeTable`\ , :py:obj:`tisserande.models.ConfigDictType`\ , :py:obj:`tisserande.models.ConfigDictTypeCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ParameterLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.ParameterTable`\ , :py:obj:`tisserande.models.Parameter`\ , :py:obj:`tisserande.models.ParameterCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ArrayLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.ArrayTable`\ , :py:obj:`tisserande.models.Array`\ , :py:obj:`tisserande.models.ArrayCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ClassLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.data_types.ClassTable`\ , :py:obj:`tisserande.models.Class`\ , :py:obj:`tisserande.models.ClassCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:data:: data_file_type

.. py:data:: config_file_type

.. py:data:: config_dict_type

.. py:data:: parameter

.. py:data:: array

.. py:data:: class_

