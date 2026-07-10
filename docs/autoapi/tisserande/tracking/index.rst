tisserande.tracking
===================

.. py:module:: tisserande.tracking


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/tisserande/tracking/annotations/index
   /autoapi/tisserande/tracking/backends/index
   /autoapi/tisserande/tracking/context/index
   /autoapi/tisserande/tracking/decorator/index
   /autoapi/tisserande/tracking/inspector/index


Attributes
----------

.. autoapisummary::

   tisserande.tracking.ArrayArg
   tisserande.tracking.ConfigDict
   tisserande.tracking.ConfigFile
   tisserande.tracking.DataFile
   tisserande.tracking.ObjectArg
   tisserande.tracking.Param
   tisserande.tracking.Untracked


Functions
---------

.. autoapisummary::

   tisserande.tracking.configure
   tisserande.tracking.track
   tisserande.tracking.track_async
   tisserande.tracking.track_shell


Package Contents
----------------

.. py:data:: ArrayArg

.. py:data:: ConfigDict

.. py:data:: ConfigFile

.. py:data:: DataFile

.. py:data:: ObjectArg

.. py:data:: Param

.. py:data:: Untracked

.. py:function:: configure(*, backend: tisserande.tracking.backends.TrackingBackend | None = None, db_url: str | None = None) -> None

   Configure the tracking system.

   Must be called before @track is used (unless a backend is passed directly
   to the decorator). If neither backend nor db_url is provided, creates a
   LocalSyncBackend with the default DB URL from config.


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


