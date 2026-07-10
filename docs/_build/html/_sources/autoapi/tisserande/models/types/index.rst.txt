tisserande.models.types
=======================

.. py:module:: tisserande.models.types

.. autoapi-nested-parse::

   Node type and execution status enumerations for the provenance graph.



Classes
-------

.. autoapisummary::

   tisserande.models.types.NodeType
   tisserande.models.types.ExecutionStatus


Module Contents
---------------

.. py:class:: NodeType(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access:

     >>> Color.RED
     <Color.RED: 1>

   - value lookup:

     >>> Color(1)
     <Color.RED: 1>

   - name lookup:

     >>> Color['RED']
     <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:attribute:: DATA_FILE
      :value: 'data_file'



   .. py:attribute:: CONFIG_FILE
      :value: 'config_file'



   .. py:attribute:: CONFIG_DICT
      :value: 'config_dict'



   .. py:attribute:: PARAMETER
      :value: 'parameter'



   .. py:attribute:: ARRAY
      :value: 'array'



   .. py:attribute:: OBJECT
      :value: 'object'



   .. py:attribute:: PYTHON_FUNCTION
      :value: 'python_function'



   .. py:attribute:: MEMBER_FUNCTION
      :value: 'member_function'



   .. py:attribute:: SHELL_FUNCTION
      :value: 'shell_function'



   .. py:property:: is_data
      :type: bool



   .. py:property:: is_logic
      :type: bool



.. py:class:: ExecutionStatus(*args, **kwds)

   Bases: :py:obj:`enum.Enum`


   Create a collection of name/value pairs.

   Example enumeration:

   >>> class Color(Enum):
   ...     RED = 1
   ...     BLUE = 2
   ...     GREEN = 3

   Access them by:

   - attribute access:

     >>> Color.RED
     <Color.RED: 1>

   - value lookup:

     >>> Color(1)
     <Color.RED: 1>

   - name lookup:

     >>> Color['RED']
     <Color.RED: 1>

   Enumerations can be iterated over, and know how many members they have:

   >>> len(Color)
   3

   >>> list(Color)
   [<Color.RED: 1>, <Color.BLUE: 2>, <Color.GREEN: 3>]

   Methods can be added to enumerations, and members can have their own
   attributes -- see the documentation for details.


   .. py:attribute:: PENDING
      :value: 'pending'



   .. py:attribute:: RUNNING
      :value: 'running'



   .. py:attribute:: SUCCESS
      :value: 'success'



   .. py:attribute:: FAILURE
      :value: 'failure'



