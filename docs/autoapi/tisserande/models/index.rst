tisserande.models
=================

.. py:module:: tisserande.models


Submodules
----------

.. toctree::
   :maxdepth: 1

   /autoapi/tisserande/models/data_types/index
   /autoapi/tisserande/models/edges/index
   /autoapi/tisserande/models/execution/index
   /autoapi/tisserande/models/function_types/index
   /autoapi/tisserande/models/nodes/index
   /autoapi/tisserande/models/types/index


Classes
-------

.. autoapisummary::

   tisserande.models.Array
   tisserande.models.ArrayCreate
   tisserande.models.Class
   tisserande.models.ClassCreate
   tisserande.models.ConfigDictType
   tisserande.models.ConfigDictTypeCreate
   tisserande.models.ConfigFileType
   tisserande.models.ConfigFileTypeCreate
   tisserande.models.DataFileType
   tisserande.models.DataFileTypeCreate
   tisserande.models.Parameter
   tisserande.models.ParameterCreate
   tisserande.models.Edge
   tisserande.models.EdgeCreate
   tisserande.models.Execution
   tisserande.models.ExecutionCreate
   tisserande.models.MemberFunction
   tisserande.models.MemberFunctionCreate
   tisserande.models.PythonFunction
   tisserande.models.PythonFunctionCreate
   tisserande.models.ShellFunction
   tisserande.models.ShellFunctionCreate
   tisserande.models.ArrayNode
   tisserande.models.ArrayNodeCreate
   tisserande.models.ConfigDictNode
   tisserande.models.ConfigDictNodeCreate
   tisserande.models.ConfigFileNode
   tisserande.models.ConfigFileNodeCreate
   tisserande.models.DataFileNode
   tisserande.models.DataFileNodeCreate
   tisserande.models.MemberFunctionNode
   tisserande.models.MemberFunctionNodeCreate
   tisserande.models.Node
   tisserande.models.NodeCreate
   tisserande.models.ObjectNode
   tisserande.models.ObjectNodeCreate
   tisserande.models.ParameterNode
   tisserande.models.ParameterNodeCreate
   tisserande.models.PythonFunctionNode
   tisserande.models.PythonFunctionNodeCreate
   tisserande.models.ShellFunctionNode
   tisserande.models.ShellFunctionNodeCreate
   tisserande.models.ExecutionStatus
   tisserande.models.NodeType


Package Contents
----------------

.. py:class:: Array(/, **data: Any)

   Bases: :py:obj:`ArrayBase`


   Array response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name', 'n_dim', 'shape']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ArrayCreate(/, **data: Any)

   Bases: :py:obj:`ArrayBase`


   Fields used to create an Array.


.. py:class:: Class(/, **data: Any)

   Bases: :py:obj:`ClassBase`


   Class response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name', 'module_']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ClassCreate(/, **data: Any)

   Bases: :py:obj:`ClassBase`


   Fields used to create a Class.


.. py:class:: ConfigDictType(/, **data: Any)

   Bases: :py:obj:`ConfigDictTypeBase`


   ConfigDictType response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ConfigDictTypeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigDictTypeBase`


   Fields used to create a ConfigDictType.


.. py:class:: ConfigFileType(/, **data: Any)

   Bases: :py:obj:`ConfigFileTypeBase`


   ConfigFileType response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ConfigFileTypeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigFileTypeBase`


   Fields used to create a ConfigFileType.


.. py:class:: DataFileType(/, **data: Any)

   Bases: :py:obj:`DataFileTypeBase`


   DataFileType response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: DataFileTypeCreate(/, **data: Any)

   Bases: :py:obj:`DataFileTypeBase`


   Fields used to create a DataFileType.


.. py:class:: Parameter(/, **data: Any)

   Bases: :py:obj:`ParameterBase`


   Parameter response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ParameterCreate(/, **data: Any)

   Bases: :py:obj:`ParameterBase`


   Fields used to create a Parameter.


.. py:class:: Edge(/, **data: Any)

   Bases: :py:obj:`EdgeBase`


   Edge response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'from_id', 'to_id', 'execution_id']



   .. py:attribute:: id_
      :type:  int
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: EdgeCreate(/, **data: Any)

   Bases: :py:obj:`EdgeBase`


   Fields used to create an Edge.


   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: Execution(/, **data: Any)

   Bases: :py:obj:`ExecutionBase`


   Execution response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'function_node_id', 'status', 'start_time', 'duration_seconds']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: function_node_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ExecutionCreate(/, **data: Any)

   Bases: :py:obj:`ExecutionBase`


   Fields used to create an Execution.


   .. py:attribute:: function_node_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: MemberFunction(/, **data: Any)

   Bases: :py:obj:`MemberFunctionBase`


   MemberFunction response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name', 'class_id']



   .. py:attribute:: id_
      :type:  int
      :value: None



   .. py:attribute:: class_id
      :type:  int
      :value: None



.. py:class:: MemberFunctionCreate(/, **data: Any)

   Bases: :py:obj:`MemberFunctionBase`


   Fields used to create a MemberFunction.


   .. py:attribute:: class_name
      :type:  str | None
      :value: None



   .. py:attribute:: class_id
      :type:  int | None
      :value: None



.. py:class:: PythonFunction(/, **data: Any)

   Bases: :py:obj:`PythonFunctionBase`


   PythonFunction response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name', 'module_']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: PythonFunctionCreate(/, **data: Any)

   Bases: :py:obj:`PythonFunctionBase`


   Fields used to create a PythonFunction.


.. py:class:: ShellFunction(/, **data: Any)

   Bases: :py:obj:`ShellFunctionBase`


   ShellFunction response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'name']



   .. py:attribute:: id_
      :type:  int
      :value: None



.. py:class:: ShellFunctionCreate(/, **data: Any)

   Bases: :py:obj:`ShellFunctionBase`


   Fields used to create a ShellFunction.


.. py:class:: ArrayNode(/, **data: Any)

   Bases: :py:obj:`ArrayNodeBase`


   ArrayNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'array_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: array_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ArrayNodeCreate(/, **data: Any)

   Bases: :py:obj:`ArrayNodeBase`


   Fields used to create an ArrayNode.


   .. py:attribute:: array_name
      :type:  str | None
      :value: None



   .. py:attribute:: array_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: ConfigDictNode(/, **data: Any)

   Bases: :py:obj:`ConfigDictNodeBase`


   ConfigDictNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'config_dict_type_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: config_dict_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ConfigDictNodeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigDictNodeBase`


   Fields used to create a ConfigDictNode.


   .. py:attribute:: config_dict_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: config_dict_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: ConfigFileNode(/, **data: Any)

   Bases: :py:obj:`ConfigFileNodeBase`


   ConfigFileNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'path', 'config_file_type_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: config_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ConfigFileNodeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigFileNodeBase`


   Fields used to create a ConfigFileNode.


   .. py:attribute:: config_file_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: config_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: DataFileNode(/, **data: Any)

   Bases: :py:obj:`DataFileNodeBase`


   DataFileNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'path', 'data_file_type_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: data_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: DataFileNodeCreate(/, **data: Any)

   Bases: :py:obj:`DataFileNodeBase`


   Fields used to create a DataFileNode.


   .. py:attribute:: data_file_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: data_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: MemberFunctionNode(/, **data: Any)

   Bases: :py:obj:`MemberFunctionNodeBase`


   MemberFunctionNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'member_function_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: member_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: MemberFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`MemberFunctionNodeBase`


   Fields used to create a MemberFunctionNode.


   .. py:attribute:: member_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: member_function_id
      :type:  int | None
      :value: None



.. py:class:: Node(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Node response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'arg_name', 'execution_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



   .. py:attribute:: path
      :type:  str | None
      :value: None



   .. py:attribute:: config_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: value_float
      :type:  float | None
      :value: None



   .. py:attribute:: value_json
      :type:  Any | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



   .. py:attribute:: data_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: config_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: config_dict_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: parameter_id
      :type:  int | None
      :value: None



   .. py:attribute:: array_id
      :type:  int | None
      :value: None



   .. py:attribute:: class_id
      :type:  int | None
      :value: None



   .. py:attribute:: python_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: member_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: shell_function_id
      :type:  int | None
      :value: None



.. py:class:: NodeCreate(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Generic node creation model.


   .. py:attribute:: path
      :type:  str | None
      :value: None



   .. py:attribute:: config_data
      :type:  dict[str, Any] | None
      :value: None



   .. py:attribute:: value_float
      :type:  float | None
      :value: None



   .. py:attribute:: value_json
      :type:  Any | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



   .. py:attribute:: data_file_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: data_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: config_file_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: config_file_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: config_dict_type_name
      :type:  str | None
      :value: None



   .. py:attribute:: config_dict_type_id
      :type:  int | None
      :value: None



   .. py:attribute:: parameter_name
      :type:  str | None
      :value: None



   .. py:attribute:: parameter_id
      :type:  int | None
      :value: None



   .. py:attribute:: array_name
      :type:  str | None
      :value: None



   .. py:attribute:: array_id
      :type:  int | None
      :value: None



   .. py:attribute:: class_name
      :type:  str | None
      :value: None



   .. py:attribute:: class_id
      :type:  int | None
      :value: None



   .. py:attribute:: python_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: python_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: member_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: member_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: shell_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: shell_function_id
      :type:  int | None
      :value: None



.. py:class:: ObjectNode(/, **data: Any)

   Bases: :py:obj:`ObjectNodeBase`


   ObjectNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'class_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: class_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ObjectNodeCreate(/, **data: Any)

   Bases: :py:obj:`ObjectNodeBase`


   Fields used to create an ObjectNode.


   .. py:attribute:: class_name
      :type:  str | None
      :value: None



   .. py:attribute:: class_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: ParameterNode(/, **data: Any)

   Bases: :py:obj:`ParameterNodeBase`


   ParameterNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'value_float', 'parameter_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: parameter_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ParameterNodeCreate(/, **data: Any)

   Bases: :py:obj:`ParameterNodeBase`


   Fields used to create a ParameterNode.


   .. py:attribute:: parameter_name
      :type:  str | None
      :value: None



   .. py:attribute:: parameter_id
      :type:  int | None
      :value: None



   .. py:attribute:: arg_name
      :type:  str | None
      :value: None



.. py:class:: PythonFunctionNode(/, **data: Any)

   Bases: :py:obj:`PythonFunctionNodeBase`


   PythonFunctionNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'python_function_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: python_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: PythonFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`PythonFunctionNodeBase`


   Fields used to create a PythonFunctionNode.


   .. py:attribute:: python_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: python_function_id
      :type:  int | None
      :value: None



.. py:class:: ShellFunctionNode(/, **data: Any)

   Bases: :py:obj:`ShellFunctionNodeBase`


   ShellFunctionNode response model.


   .. py:attribute:: model_config

      Configuration for the model, should be a dictionary conforming to [`ConfigDict`][pydantic.config.ConfigDict].


   .. py:attribute:: col_names_for_table
      :type:  ClassVar[list[str]]
      :value: ['id_', 'type_', 'shell_function_id']



   .. py:attribute:: id_
      :type:  uuid.UUID


   .. py:attribute:: shell_function_id
      :type:  int | None
      :value: None



   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



.. py:class:: ShellFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`ShellFunctionNodeBase`


   Fields used to create a ShellFunctionNode.


   .. py:attribute:: shell_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: shell_function_id
      :type:  int | None
      :value: None



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



