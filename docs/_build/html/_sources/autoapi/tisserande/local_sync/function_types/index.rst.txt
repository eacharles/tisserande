tisserande.local_sync.function_types
====================================

.. py:module:: tisserande.local_sync.function_types


Attributes
----------

.. autoapisummary::

   tisserande.local_sync.function_types.python_function
   tisserande.local_sync.function_types.member_function
   tisserande.local_sync.function_types.shell_function


Classes
-------

.. autoapisummary::

   tisserande.local_sync.function_types.PythonFunctionSyncOperations
   tisserande.local_sync.function_types.MemberFunctionSyncOperations
   tisserande.local_sync.function_types.ShellFunctionSyncOperations


Module Contents
---------------

.. py:class:: PythonFunctionSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.function_types.PythonFunctionTable`\ , :py:obj:`tisserande.models.PythonFunction`\ , :py:obj:`tisserande.models.PythonFunctionCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: MemberFunctionSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.function_types.MemberFunctionTable`\ , :py:obj:`tisserande.models.MemberFunction`\ , :py:obj:`tisserande.models.MemberFunctionCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:class:: ShellFunctionSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.function_types.ShellFunctionTable`\ , :py:obj:`tisserande.models.ShellFunction`\ , :py:obj:`tisserande.models.ShellFunctionCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:data:: python_function

.. py:data:: member_function

.. py:data:: shell_function

