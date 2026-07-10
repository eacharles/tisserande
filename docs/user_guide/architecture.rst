Architecture
============

Tisserande is built as a layered architecture on top of the `macon
<https://github.com/eacharles/macon>`_ CRUD framework.

Layer Diagram
-------------

.. code-block:: text

   Tracking Decorators (@track, @track_async, track_shell)
     └── TrackingContext + ArgumentInspector
           └── TrackingBackend (LocalSyncBackend / NullBackend)
                 └── local_sync (SyncOperations)
                       └── local_async (LocalOperations)
                             └── db_oper (TableOperations)
                                   └── macon.db_funcs (raw SQLAlchemy queries)
                                         └── macon.db (Base, session)

Layer Responsibilities
----------------------

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Layer
     - Purpose
   * - ``models/``
     - Pydantic models for validation and serialization (Base/Create/Response triplets)
   * - ``db/``
     - SQLAlchemy ORM table definitions
   * - ``db_oper/``
     - ``TableOperations`` subclasses with FK resolution logic
   * - ``local_async/``
     - ``LocalOperations`` wrappers adding session management (``@with_session``)
   * - ``local_sync/``
     - ``SyncOperations`` wrappers adding ``asyncio.run()`` for non-async contexts
   * - ``tracking/``
     - Decorators, argument inspection, backends, execution lifecycle
   * - ``router/``
     - FastAPI application with auto-generated CRUD endpoints
   * - ``cli/``
     - Click CLI entry points for admin tasks

Domain Model
------------

The provenance graph consists of three entity types:

**Nodes** — vertices in the DAG, stored in a single table with a ``type_``
discriminator column:

- *Data nodes*: ``data_file``, ``config_file``, ``config_dict``, ``parameter``,
  ``array``, ``object``
- *Logic nodes*: ``python_function``, ``member_function``, ``shell_function``

**Edges** — directed links between nodes:

- Data → Logic = "this data is an input to this function"
- Logic → Data = "this function produced this data"

**Executions** — groups all nodes and edges from a single function call, with
timing information and status.

Database Schema
---------------

.. code-block:: text

   ┌─────────────────┐     ┌──────────────┐     ┌──────────────────┐
   │  Type Tables    │     │    node      │     │    execution     │
   │  (int PK)       │◄────│  (UUID PK)   │────►│   (UUID PK)      │
   │                 │     │  type_       │     │   status         │
   │  data_file_type │     │  path        │     │   start_time     │
   │  config_file_..│     │  value_float │     │   duration_secs  │
   │  parameter      │     │  value_json  │     │   error_message  │
   │  python_func.. │     │  arg_name    │     └──────────────────┘
   │  ...            │     │  execution_id│
   └─────────────────┘     └──────────────┘
                                  ▲  ▲
                                  │  │
                           ┌──────┘  └──────┐
                           │    edge        │
                           │  (int PK)      │
                           │  from_id (FK)  │
                           │  to_id (FK)    │
                           │  execution_id  │
                           └────────────────┘

Design decisions:

- **Single Node table** with nullable type-specific columns — simplifies graph
  queries since edges reference only one table.
- **UUID7 primary keys** for nodes and executions — time-ordered and globally unique.
- **Integer primary keys** for type tables and edges — low-cardinality or high-volume.
