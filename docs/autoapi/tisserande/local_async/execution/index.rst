tisserande.local_async.execution
================================

.. py:module:: tisserande.local_async.execution


Attributes
----------

.. autoapisummary::

   tisserande.local_async.execution.execution


Classes
-------

.. autoapisummary::

   tisserande.local_async.execution.ExecutionLocalOperations


Module Contents
---------------

.. py:class:: ExecutionLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.execution.ExecutionTable`\ , :py:obj:`tisserande.models.Execution`\ , :py:obj:`tisserande.models.ExecutionCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:data:: execution

