Tracking Decorators
===================

The tracking system is the core feature of tisserande. It provides decorators
that automatically record provenance when functions are called.

Setup
-----

Before using ``@track``, configure the tracking system:

.. code-block:: python

   from tisserande.tracking import configure

   # Option 1: Use a database URL (creates tables automatically)
   configure(db_url="sqlite+aiosqlite:///provenance.db")

   # Option 2: Use a custom backend
   from tisserande.tracking.backends import NullBackend
   configure(backend=NullBackend())

If ``configure()`` is not called, decorated functions execute normally without
any tracking (the decorator is a transparent no-op).

The ``@track`` Decorator
------------------------

For synchronous functions:

.. code-block:: python

   from tisserande.tracking import track

   @track
   def my_function(x: float, y: float) -> float:
       return x + y

Can also be called with options:

.. code-block:: python

   @track(track_inputs=True, track_outputs=True)
   def my_function(x: float, y: float) -> float:
       return x + y

Options:

- ``track_inputs`` (default: ``True``) — whether to create nodes for input arguments
- ``track_outputs`` (default: ``True``) — whether to create nodes for return values
- ``backend`` — override the global backend for this specific function

The ``@track_async`` Decorator
------------------------------

For async functions:

.. code-block:: python

   from tisserande.tracking import track_async

   @track_async
   async def fetch_and_process(url: str) -> str:
       data = await fetch(url)
       return await process(data)

Same options as ``@track``.

The ``track_shell()`` Function
------------------------------

For shell commands:

.. code-block:: python

   from tisserande.tracking import track_shell

   result = track_shell(
       "python train.py --epochs 100",
       inputs={"script": "train.py", "epochs": 100},
       outputs={"model": "/models/trained.pt"},
   )

   if result.returncode == 0:
       print("Success!")

Parameters:

- ``command`` — shell command string or list of arguments
- ``inputs`` — dict mapping names to values (tracked as input data nodes)
- ``outputs`` — dict mapping names to values (tracked as output data nodes)
- ``backend`` — override the global backend

What Gets Recorded
------------------

For each tracked function call:

1. An **Execution** record is created with status ``RUNNING``
2. A **function node** is created (type: ``python_function`` or ``shell_function``)
3. For each tracked input argument:
   - A **data node** is created (classified by type annotation or heuristic)
   - An **edge** is created: input node → function node
4. The function executes
5. For each return value:
   - A **data node** is created for the output
   - An **edge** is created: function node → output node
6. The Execution is updated with status (``SUCCESS`` or ``FAILURE``),
   duration, and error info if applicable

Error Handling
--------------

If the tracked function raises an exception:

- The exception **propagates normally** (tracking doesn't suppress errors)
- The Execution is marked as ``FAILURE``
- The error message and full traceback are stored
- No output nodes or edges are created

.. code-block:: python

   @track
   def risky_function(x: float) -> float:
       if x < 0:
           raise ValueError("x must be non-negative")
       return x ** 0.5

   try:
       risky_function(-1)
   except ValueError:
       pass  # Exception propagates; execution recorded as FAILURE
