Command-Line Interface
======================

Tisserande provides two CLI entry points:

- ``tisserande-local`` — local database administration
- ``tisserande-server`` — start the REST API server

tisserande-local
----------------

The local CLI provides CRUD commands for all provenance tables:

.. code-block:: bash

   tisserande-local --help

Each table has its own command group with standard operations:

.. code-block:: bash

   # List executions
   tisserande-local execution get-rows

   # Get a specific execution
   tisserande-local execution get-row <uuid>

   # List nodes
   tisserande-local node get-rows --limit 20

   # Filter nodes by type
   tisserande-local node filter-rows --filter "type_:eq:data_file"

   # List python functions
   tisserande-local python-function get-rows

   # Create a data file type
   tisserande-local data-file-type create-row --name fits

Available table groups:

- ``data-file-type``
- ``config-file-type``
- ``config-dict-type``
- ``parameter``
- ``array``
- ``class``
- ``python-function``
- ``member-function``
- ``shell-function``
- ``node``
- ``edge``
- ``execution``

tisserande-server
-----------------

Start the FastAPI server:

.. code-block:: bash

   tisserande-server --host 0.0.0.0 --port 8080

   # With auto-reload for development
   tisserande-server --reload

   # Without reload for production
   tisserande-server --no-reload

The server provides REST API endpoints for all tables. Visit
``http://localhost:8080/docs`` for the interactive Swagger UI documentation.

Environment Setup
-----------------

Set the database URL before using the CLI:

.. code-block:: bash

   export TISSERANDE__DB__URL="sqlite+aiosqlite:///provenance.db"

   # Then use the CLI
   tisserande-local execution get-rows
