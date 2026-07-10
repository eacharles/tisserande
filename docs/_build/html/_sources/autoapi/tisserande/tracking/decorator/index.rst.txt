tisserande.tracking.decorator
=============================

.. py:module:: tisserande.tracking.decorator

.. autoapi-nested-parse::

   Tracking decorators: @track, @track_async, and track_shell().

   These are the primary user-facing API for automatic provenance capture.



Attributes
----------

.. autoapisummary::

   tisserande.tracking.decorator.F


Functions
---------

.. autoapisummary::

   tisserande.tracking.decorator.configure
   tisserande.tracking.decorator.get_backend
   tisserande.tracking.decorator.track
   tisserande.tracking.decorator.track_async
   tisserande.tracking.decorator.track_shell


Module Contents
---------------

.. py:data:: F

.. py:function:: configure(*, backend: tisserande.tracking.backends.TrackingBackend | None = None, db_url: str | None = None) -> None

   Configure the tracking system.

   Must be called before @track is used (unless a backend is passed directly
   to the decorator). If neither backend nor db_url is provided, creates a
   LocalSyncBackend with the default DB URL from config.


.. py:function:: get_backend() -> tisserande.tracking.backends.TrackingBackend | None

   Get the currently configured backend.


.. py:function:: track(func: F) -> F
                 track(*, backend: tisserande.tracking.backends.TrackingBackend | None = None, track_inputs: bool = True, track_outputs: bool = True) -> collections.abc.Callable[[F], F]

   Decorator to track execution provenance of a sync function.

   Can be used with or without arguments:
       @track
       def my_func(...): ...

       @track(track_outputs=False)
       def my_func(...): ...


.. py:function:: track_async(func: F) -> F
                 track_async(*, backend: tisserande.tracking.backends.TrackingBackend | None = None, track_inputs: bool = True, track_outputs: bool = True) -> collections.abc.Callable[[F], F]

   Decorator to track execution provenance of an async function.


.. py:function:: track_shell(command: str | list[str], *, inputs: dict[str, Any] | None = None, outputs: dict[str, Any] | None = None, backend: tisserande.tracking.backends.TrackingBackend | None = None) -> subprocess.CompletedProcess[str]

   Execute and track a shell command.

   :param command: Shell command to execute
   :param inputs: Dict mapping arg names to values (tracked as input data nodes)
   :param outputs: Dict mapping output names to values (tracked as output data nodes)


