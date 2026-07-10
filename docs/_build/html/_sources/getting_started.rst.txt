Getting Started
===============

Installation
------------

Install tisserande with all optional dependencies:

.. code-block:: bash

   pip install tisserande[all]

Or install only what you need:

.. code-block:: bash

   pip install tisserande            # Core tracking + SQLite backend
   pip install tisserande[server]    # FastAPI server
   pip install tisserande[numpy]     # NumPy array support

Quick Start
-----------

1. Configure the tracking system:

.. code-block:: python

   from tisserande.tracking import configure

   configure(db_url="sqlite+aiosqlite:///provenance.db")

2. Decorate your functions:

.. code-block:: python

   from tisserande.tracking import track
   from tisserande.tracking.annotations import DataFile, Param

   @track
   def fit_model(
       input_catalog: DataFile[str],
       learning_rate: Param[float],
   ) -> DataFile[str]:
       # ... your code ...
       return "/data/results/model.fits"

   # Call normally — provenance is recorded automatically
   fit_model("/data/catalogs/train.fits", 0.01)

3. Query the provenance:

.. code-block:: python

   from tisserande.local_sync import execution, node, edge

   # List all executions
   for ex in execution.get_rows():
       print(f"{ex.id_}: status={ex.status}, duration={ex.duration_seconds:.2f}s")

   # Get all nodes
   all_nodes = node.get_rows()

What Gets Recorded
------------------

When a tracked function is called, tisserande creates:

- An **Execution** record with timing, status, and error info
- A **function node** representing the function itself
- **Input nodes** for each tracked argument (classified by type)
- **Output nodes** for the return value(s)
- **Edges** connecting inputs → function → outputs

.. code-block:: text

   [/data/train.fits]  ──→  [fit_model()]  ──→  [/data/model.fits]
   [lr=0.01]  ─────────┘

All records are linked to the same Execution, making it easy to query
"what happened in this function call?"

Tracking Shell Commands
-----------------------

For non-Python processes, use ``track_shell()``:

.. code-block:: python

   from tisserande.tracking import track_shell

   result = track_shell(
       "sextractor input.fits -c config.sex",
       inputs={
           "image": "/data/input.fits",
           "config": "/configs/config.sex",
       },
       outputs={
           "catalog": "/data/output.cat",
       },
   )
   print(result.returncode)  # 0 on success

Async Functions
---------------

For async code, use ``@track_async``:

.. code-block:: python

   from tisserande.tracking import track_async

   @track_async
   async def download_and_process(url: str) -> DataFile[str]:
       data = await fetch(url)
       output_path = "/tmp/processed.fits"
       await write_fits(output_path, data)
       return output_path

Disabling Tracking
------------------

For tests or performance-critical code, use the ``NullBackend``:

.. code-block:: python

   from tisserande.tracking import configure
   from tisserande.tracking.backends import NullBackend

   configure(backend=NullBackend())

Or disable globally via environment variable:

.. code-block:: bash

   export TISSERANDE__TRACKING__ENABLED=false
