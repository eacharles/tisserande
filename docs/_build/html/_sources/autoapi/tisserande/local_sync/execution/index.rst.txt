tisserande.local_sync.execution
===============================

.. py:module:: tisserande.local_sync.execution


Attributes
----------

.. autoapisummary::

   tisserande.local_sync.execution.execution


Classes
-------

.. autoapisummary::

   tisserande.local_sync.execution.ExecutionSyncOperations


Module Contents
---------------

.. py:class:: ExecutionSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.execution.ExecutionTable`\ , :py:obj:`tisserande.models.Execution`\ , :py:obj:`tisserande.models.ExecutionCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:data:: execution

