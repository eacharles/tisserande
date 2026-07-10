tisserande.local_sync.data_types
================================

.. py:module:: tisserande.local_sync.data_types


Attributes
----------

.. autoapisummary::

   tisserande.local_sync.data_types.data_file_type
   tisserande.local_sync.data_types.config_file_type
   tisserande.local_sync.data_types.config_dict_type
   tisserande.local_sync.data_types.parameter
   tisserande.local_sync.data_types.array
   tisserande.local_sync.data_types.class_


Classes
-------

.. autoapisummary::

   tisserande.local_sync.data_types.DataFileTypeSyncOperations
   tisserande.local_sync.data_types.ConfigFileTypeSyncOperations
   tisserande.local_sync.data_types.ConfigDictTypeSyncOperations
   tisserande.local_sync.data_types.ParameterSyncOperations
   tisserande.local_sync.data_types.ArraySyncOperations
   tisserande.local_sync.data_types.ClassSyncOperations


Module Contents
---------------

.. py:class:: DataFileTypeSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.DataFileTypeTable`\ , :py:obj:`tisserande.models.DataFileType`\ , :py:obj:`tisserande.models.DataFileTypeCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ConfigFileTypeSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigFileTypeTable`\ , :py:obj:`tisserande.models.ConfigFileType`\ , :py:obj:`tisserande.models.ConfigFileTypeCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ConfigDictTypeSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigDictTypeTable`\ , :py:obj:`tisserande.models.ConfigDictType`\ , :py:obj:`tisserande.models.ConfigDictTypeCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ParameterSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.ParameterTable`\ , :py:obj:`tisserande.models.Parameter`\ , :py:obj:`tisserande.models.ParameterCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ArraySyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.ArrayTable`\ , :py:obj:`tisserande.models.Array`\ , :py:obj:`tisserande.models.ArrayCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ClassSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.data_types.ClassTable`\ , :py:obj:`tisserande.models.Class`\ , :py:obj:`tisserande.models.ClassCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:data:: data_file_type

.. py:data:: config_file_type

.. py:data:: config_dict_type

.. py:data:: parameter

.. py:data:: array

.. py:data:: class_

