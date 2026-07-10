tisserande.tracking.backends
============================

.. py:module:: tisserande.tracking.backends

.. autoapi-nested-parse::

   Pluggable storage backends for provenance records.

   The TrackingBackend protocol defines the interface; concrete implementations
   include LocalSyncBackend (real DB) and NullBackend (no-op for testing).



Classes
-------

.. autoapisummary::

   tisserande.tracking.backends.TrackingBackend
   tisserande.tracking.backends.LocalSyncBackend
   tisserande.tracking.backends.NullBackend


Module Contents
---------------

.. py:class:: TrackingBackend

   Bases: :py:obj:`Protocol`


   Protocol for provenance storage backends.


   .. py:method:: create_execution(**kwargs: Any) -> uuid.UUID


   .. py:method:: update_execution(execution_id: uuid.UUID, **kwargs: Any) -> None


   .. py:method:: create_node(**kwargs: Any) -> uuid.UUID


   .. py:method:: create_edge(from_id: uuid.UUID, to_id: uuid.UUID, execution_id: uuid.UUID) -> int


.. py:class:: LocalSyncBackend

   Uses tisserande.local_sync to store provenance in the local DB.


   .. py:method:: create_execution(**kwargs: Any) -> uuid.UUID


   .. py:method:: update_execution(execution_id: uuid.UUID, **kwargs: Any) -> None


   .. py:method:: create_node(**kwargs: Any) -> uuid.UUID


   .. py:method:: create_edge(from_id: uuid.UUID, to_id: uuid.UUID, execution_id: uuid.UUID) -> int


.. py:class:: NullBackend

   Discards all provenance. Useful for testing or disabling tracking.


   .. py:method:: create_execution(**kwargs: Any) -> uuid.UUID


   .. py:method:: update_execution(execution_id: uuid.UUID, **kwargs: Any) -> None


   .. py:method:: create_node(**kwargs: Any) -> uuid.UUID


   .. py:method:: create_edge(from_id: uuid.UUID, to_id: uuid.UUID, execution_id: uuid.UUID) -> int


