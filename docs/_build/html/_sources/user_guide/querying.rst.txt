Querying Provenance
===================

Once provenance is recorded, you can query the database using tisserande's
layered operations.

Synchronous Queries
-------------------

For scripts and CLI tools, use the ``local_sync`` layer:

.. code-block:: python

   from tisserande.local_sync import execution, node, edge

   # Get all executions
   all_executions = execution.get_rows()

   # Get a specific execution by ID
   ex = execution.get_row(some_uuid)

   # Get all nodes for an execution
   from macon.models import Filter, FilterOp
   exec_nodes = node.filter_rows(
       filters=[Filter(field="execution_id", op=FilterOp.EQ, value=str(some_uuid))]
   )

   # Get all edges for an execution
   exec_edges = edge.filter_rows(
       filters=[Filter(field="execution_id", op=FilterOp.EQ, value=str(some_uuid))]
   )

Async Queries
-------------

For async contexts (e.g., inside a FastAPI endpoint), use the ``local_async`` layer:

.. code-block:: python

   from tisserande.local_async import execution, node, edge

   all_executions = await execution.get_rows()
   ex = await execution.get_row(some_uuid)

Available Operations
--------------------

All table operations support the full macon CRUD interface:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Method
     - Description
   * - ``get_row(id)``
     - Get a single record by primary key
   * - ``get_row_by_name(name)``
     - Get a record by unique name (type tables only)
   * - ``get_rows(limit, offset)``
     - Get multiple records with pagination
   * - ``create_row(**kwargs)``
     - Create a new record
   * - ``update_row(id, **kwargs)``
     - Update an existing record
   * - ``delete_row(id)``
     - Delete a record
   * - ``filter_rows(filters, order_by)``
     - Filter records with operators (eq, ne, lt, gt, like, etc.)
   * - ``count_rows()``
     - Count total records

Available Tables
----------------

Each table is accessible as a module-level instance:

**Type tables** (lookup tables):

- ``data_file_type`` — types of data files
- ``config_file_type`` — types of config files
- ``config_dict_type`` — types of config dicts
- ``parameter`` — parameter definitions
- ``array`` — array definitions
- ``class_`` — Python class definitions
- ``python_function`` — Python function definitions
- ``member_function`` — member function definitions
- ``shell_function`` — shell function definitions

**Core provenance tables**:

- ``node`` — all provenance graph nodes
- ``edge`` — all provenance graph edges
- ``execution`` — all execution records

Example: Trace a File's Lineage
-------------------------------

Find all executions that produced a given output file:

.. code-block:: python

   from tisserande.local_sync import node, edge
   from macon.models import Filter, FilterOp

   # Find the node for our output file
   output_nodes = node.filter_rows(
       filters=[
           Filter(field="type_", op=FilterOp.EQ, value="data_file"),
           Filter(field="path", op=FilterOp.EQ, value="/data/output.fits"),
       ]
   )

   # Find edges pointing TO this node (from a function)
   for output_node in output_nodes:
       incoming_edges = edge.filter_rows(
           filters=[Filter(field="to_id", op=FilterOp.EQ, value=str(output_node.id_))]
       )
       for e in incoming_edges:
           # e.from_id is the function node that produced this output
           func_node = node.get_row(e.from_id)
           print(f"Produced by execution: {func_node.execution_id}")
