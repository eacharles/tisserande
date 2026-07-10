tisserande.local_sync.nodes
===========================

.. py:module:: tisserande.local_sync.nodes


Attributes
----------

.. autoapisummary::

   tisserande.local_sync.nodes.node


Classes
-------

.. autoapisummary::

   tisserande.local_sync.nodes.NodeSyncOperations


Module Contents
---------------

.. py:class:: NodeSyncOperations(async_ops: macon.local_async.base.LocalOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_sync.base.SyncOperations`\ [\ :py:obj:`tisserande.db.nodes.NodeTable`\ , :py:obj:`tisserande.models.Node`\ , :py:obj:`tisserande.models.NodeCreate`\ ]


   Synchronous wrapper for local operations.

   Wraps async LocalOperations methods to provide synchronous versions
   for use in non-async contexts like CLI commands or scripts.

   WARNING: These methods use asyncio.run() internally and cannot be
   called from within an already-running event loop.


.. py:data:: node

