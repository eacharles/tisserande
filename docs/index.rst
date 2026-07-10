tisserande
==========

**tisserande** is a Python package for tracking execution provenance of Python
functions and shell scripts. It records what functions were called, what data they
consumed and produced, and how long they took — all as a directed acyclic graph
(DAG) stored in a database.

The name comes from the French word for "weaver" — tisserande weaves together the
threads of your computational pipeline into a traceable provenance fabric.

.. toctree::
   :maxdepth: 2
   :caption: Contents

   getting_started
   user_guide/index
   api/index

Features
--------

- **Automatic provenance capture** — decorate functions with ``@track`` and get
  full DAG recording of inputs, outputs, and execution metadata
- **Type-annotated tracking** — use ``DataFile[str]``, ``Param[float]``, etc. to
  explicitly classify arguments, or let heuristics do it automatically
- **Shell command tracking** — ``track_shell()`` for non-Python processes
- **Async support** — ``@track_async`` for async functions
- **Full REST API** — auto-generated CRUD endpoints for all provenance tables
- **CLI tools** — command-line admin for querying and managing provenance data
- **Pluggable backends** — swap storage implementations without changing your code
- **Built on macon** — inherits production-quality CRUD framework with filtering,
  pagination, lifecycle hooks, and full type safety
