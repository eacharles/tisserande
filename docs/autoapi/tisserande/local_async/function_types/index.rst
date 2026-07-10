tisserande.local_async.function_types
=====================================

.. py:module:: tisserande.local_async.function_types


Attributes
----------

.. autoapisummary::

   tisserande.local_async.function_types.python_function
   tisserande.local_async.function_types.member_function
   tisserande.local_async.function_types.shell_function


Classes
-------

.. autoapisummary::

   tisserande.local_async.function_types.PythonFunctionLocalOperations
   tisserande.local_async.function_types.MemberFunctionLocalOperations
   tisserande.local_async.function_types.ShellFunctionLocalOperations


Module Contents
---------------

.. py:class:: PythonFunctionLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.function_types.PythonFunctionTable`\ , :py:obj:`tisserande.models.PythonFunction`\ , :py:obj:`tisserande.models.PythonFunctionCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: MemberFunctionLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.function_types.MemberFunctionTable`\ , :py:obj:`tisserande.models.MemberFunction`\ , :py:obj:`tisserande.models.MemberFunctionCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:class:: ShellFunctionLocalOperations(table_operations: macon.db_oper.base.TableOperations[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.local_async.base.LocalOperations`\ [\ :py:obj:`tisserande.db.function_types.ShellFunctionTable`\ , :py:obj:`tisserande.models.ShellFunction`\ , :py:obj:`tisserande.models.ShellFunctionCreate`\ ]


   Base class for table-specific local operations.

   Dynamically binds API functions as methods on this instance,
   pre-bound with the table operations. All methods are async.

   .. rubric:: Examples

   >>> from rail_svc.local import algorithm
   >>>
   >>> # In async context
   >>> algo = await algorithm.get_row(row_id=1)
   >>> algos = await algorithm.get_rows(limit=10)


.. py:data:: python_function

.. py:data:: member_function

.. py:data:: shell_function

