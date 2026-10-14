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

**Nodes** — vertices in the DAG. A base ``node`` table holds shared columns
(``id_``, ``type_``, ``execution_id``, ``arg_name``) and per-type subtables are
joined via SQLAlchemy's joined-table inheritance:

- *Data nodes*: ``data_file``, ``config_file``, ``config_dict``, ``parameter``,
  ``array``, ``object``, ``ceci_file``
- *Logic nodes*: ``python_function``, ``member_function``, ``shell_function``,
  ``ceci_stage``

**Edges** — directed links between nodes:

- Data → Logic = "this data is an input to this function"
- Logic → Data = "this function produced this data"

**Executions** — groups all nodes and edges from a single function call or
pipeline run, with timing, status, and optional ``parent_execution_id`` for
nesting stage executions inside a pipeline execution.

**CECI pipeline tables** — schema-level records for DESC/CECI pipelines (not
part of the DAG, but used to annotate instance nodes):

- ``ceci_pipeline`` — pipeline definition (name, YAML structure, default config)
- ``ceci_pipeline_variant`` — a config override set on a base pipeline
- ``ceci_pipeline_instance`` — a specific pipeline run (date, status, variant FK)
- ``ceci_pipeline_stage_assoc`` — many-to-many between pipeline and schema stage nodes

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

- **Joined-table inheritance** for nodes — a base ``node`` table with per-type
  subtables (``data_file_node``, ``ceci_stage_node``, etc.) keeps graph queries
  simple: edges always FK to ``node.id_``.
- **Schema vs instance nodes** — a node with ``execution_id=None`` is a schema
  node (class or file type definition); one with ``execution_id`` set is an
  instance node from a specific run. The same table and model serve both roles.
- **UUID7 primary keys** for nodes and executions — time-ordered and globally unique.
- **Integer primary keys** for type/pipeline tables and edges — low-cardinality
  or high-volume write paths.
