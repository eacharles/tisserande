tisserande.local_async.edges
============================

.. py:module:: tisserande.local_async.edges


Attributes
----------

.. autoapisummary::

   tisserande.local_async.edges.edge


Classes
-------

.. autoapisummary::

   tisserande.local_async.edges.EdgeLocalOperations


Module Contents
---------------

.. py:class:: EdgeLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.edges.EdgeTable`\ , :py:obj:`tisserande.models.Edge`\ , :py:obj:`tisserande.models.EdgeCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:data:: edge

