tisserande.tracking.context
===========================

.. py:module:: tisserande.tracking.context

.. autoapi-nested-parse::

   Execution context that orchestrates provenance recording for one function call.



Classes
-------

.. autoapisummary::

   tisserande.tracking.context.TrackingContext


Module Contents
---------------

.. py:class:: TrackingContext(backend: tisserande.tracking.backends.TrackingBackend)

   Manages the lifecycle of a single execution being tracked.


   .. py:method:: start_execution(inspector: tisserande.tracking.inspector.ArgumentInspector, args: tuple[Any, Ellipsis], kwargs: dict[str, Any]) -> None

      Create Execution + function node + input nodes + input edges.



   .. py:method:: finish_execution(inspector: tisserande.tracking.inspector.ArgumentInspector, result: Any, exception: BaseException | None = None) -> None

      Create output nodes + output edges, update Execution with timing/status.



