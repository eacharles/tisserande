Configuration
=============

Tisserande is configured via environment variables or programmatically.

Environment Variables
---------------------

All environment variables use the prefix ``TISSERANDE__`` with ``__`` as the
nested delimiter:

.. list-table::
   :header-rows: 1
   :widths: 35 25 40

   * - Variable
     - Default
     - Description
   * - ``TISSERANDE__DB__URL``
     - ``sqlite+aiosqlite:///tisserande.db``
     - Database connection URL
   * - ``TISSERANDE__DB__ECHO``
     - ``false``
     - SQLAlchemy engine echo (SQL logging)
   * - ``TISSERANDE__TRACKING__ENABLED``
     - ``true``
     - Global toggle for provenance tracking
   * - ``TISSERANDE__TRACKING__BACKEND``
     - ``local_sync``
     - Default backend (``local_sync`` or ``null``)
   * - ``TISSERANDE__TRACKING__AUTO_CLASSIFY``
     - ``true``
     - Auto-classify unannoted arguments using heuristics

Database URL Examples
---------------------

.. code-block:: bash

   # SQLite (default, good for single-user)
   export TISSERANDE__DB__URL="sqlite+aiosqlite:///provenance.db"

   # In-memory SQLite (for testing)
   export TISSERANDE__DB__URL="sqlite+aiosqlite://"

   # PostgreSQL
   export TISSERANDE__DB__URL="postgresql+asyncpg://user:pass@localhost:5432/provenance"

Programmatic Configuration
--------------------------

Use ``configure()`` to set up the tracking system in code:

.. code-block:: python

   from tisserande.tracking import configure

   # With a database URL
   configure(db_url="sqlite+aiosqlite:///my_provenance.db")

   # With a custom backend
   from tisserande.tracking.backends import NullBackend
   configure(backend=NullBackend())

The ``configure()`` function:

1. Initializes the database engine
2. Creates all tables (if they don't exist)
3. Sets the default backend for all ``@track`` decorators

Configuration Object
--------------------

Access the configuration programmatically:

.. code-block:: python

   from tisserande.config import config

   print(config.db.url)
   print(config.tracking.enabled)
   print(config.tracking.backend)

The ``Configuration`` class uses Pydantic Settings, so values can come from:

- Environment variables (highest priority)
- Default values in the class definition

Backends
--------

Tisserande supports pluggable backends:

**LocalSyncBackend** (default)
   Stores provenance directly in the configured database using synchronous
   operations (``asyncio.run()`` internally). Best for scripts and CLI tools.

**NullBackend**
   Discards all provenance. Use for:

   - Unit tests where you don't want DB overhead
   - Performance-critical code paths
   - Temporarily disabling tracking

Custom backends can be created by implementing the ``TrackingBackend`` protocol:

.. code-block:: python

   from typing import Any
   from uuid import UUID

   class MyBackend:
       def create_execution(self, **kwargs: Any) -> UUID: ...
       def update_execution(self, execution_id: UUID, **kwargs: Any) -> None: ...
       def create_node(self, **kwargs: Any) -> UUID: ...
       def create_edge(self, from_id: UUID, to_id: UUID, execution_id: UUID) -> int: ...
