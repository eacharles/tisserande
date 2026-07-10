tisserande.local_sync.edges
===========================

.. py:module:: tisserande.local_sync.edges


Attributes
----------

.. autoapisummary::

   tisserande.local_sync.edges.edge


Classes
-------

.. autoapisummary::

   tisserande.local_sync.edges.EdgeSyncOperations


Module Contents
---------------

.. py:class:: EdgeSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.edges.EdgeTable`\ , :py:obj:`tisserande.models.Edge`\ , :py:obj:`tisserande.models.EdgeCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:data:: edge

