tisserande.models.nodes
=======================

.. py:module:: tisserande.models.nodes

.. autoapi-nested-parse::

   Pydantic models for provenance graph nodes (data nodes and logic nodes).



Classes
-------

.. autoapisummary::

   tisserande.models.nodes.NodeBase
   tisserande.models.nodes.NodeCreate
   tisserande.models.nodes.Node
   tisserande.models.nodes.DataFileNodeBase
   tisserande.models.nodes.DataFileNodeCreate
   tisserande.models.nodes.DataFileNode
   tisserande.models.nodes.ConfigFileNodeBase
   tisserande.models.nodes.ConfigFileNodeCreate
   tisserande.models.nodes.ConfigFileNode
   tisserande.models.nodes.ConfigDictNodeBase
   tisserande.models.nodes.ConfigDictNodeCreate
   tisserande.models.nodes.ConfigDictNode
   tisserande.models.nodes.ParameterNodeBase
   tisserande.models.nodes.ParameterNodeCreate
   tisserande.models.nodes.ParameterNode
   tisserande.models.nodes.ArrayNodeBase
   tisserande.models.nodes.ArrayNodeCreate
   tisserande.models.nodes.ArrayNode
   tisserande.models.nodes.ObjectNodeBase
   tisserande.models.nodes.ObjectNodeCreate
   tisserande.models.nodes.ObjectNode
   tisserande.models.nodes.PythonFunctionNodeBase
   tisserande.models.nodes.PythonFunctionNodeCreate
   tisserande.models.nodes.PythonFunctionNode
   tisserande.models.nodes.MemberFunctionNodeBase
   tisserande.models.nodes.MemberFunctionNodeCreate
   tisserande.models.nodes.MemberFunctionNode
   tisserande.models.nodes.ShellFunctionNodeBase
   tisserande.models.nodes.ShellFunctionNodeCreate
   tisserande.models.nodes.ShellFunctionNode


Module Contents
---------------

.. py:class:: NodeBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Base model for all graph nodes.


   .. py:attribute:: type_
      :type:  tisserande.models.types.NodeType
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



.. py:class:: DataFileNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a data file node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.DATA_FILE]


   .. py:attribute:: path
      :type:  str
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



.. py:class:: ConfigFileNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a config file node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.CONFIG_FILE]


   .. py:attribute:: path
      :type:  str
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



.. py:class:: ConfigDictNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a config dict node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.CONFIG_DICT]


   .. py:attribute:: config_data
      :type:  dict[str, Any]
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



.. py:class:: ParameterNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a parameter node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.PARAMETER]


   .. py:attribute:: value_float
      :type:  float
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



.. py:class:: ArrayNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for an array node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.ARRAY]


   .. py:attribute:: value_json
      :type:  list[float] | list[list[float]]
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



.. py:class:: ObjectNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a python object node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.OBJECT]


   .. py:attribute:: value_json
      :type:  Any
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



.. py:class:: PythonFunctionNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a python function node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.PYTHON_FUNCTION]


.. py:class:: PythonFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`PythonFunctionNodeBase`


   Fields used to create a PythonFunctionNode.


   .. py:attribute:: python_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: python_function_id
      :type:  int | None
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



.. py:class:: MemberFunctionNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a member function node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.MEMBER_FUNCTION]


.. py:class:: MemberFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`MemberFunctionNodeBase`


   Fields used to create a MemberFunctionNode.


   .. py:attribute:: member_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: member_function_id
      :type:  int | None
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



.. py:class:: ShellFunctionNodeBase(/, **data: Any)

   Bases: :py:obj:`NodeBase`


   Model for a shell function node.


   .. py:attribute:: type_
      :type:  Literal[tisserande.models.types.NodeType.SHELL_FUNCTION]


.. py:class:: ShellFunctionNodeCreate(/, **data: Any)

   Bases: :py:obj:`ShellFunctionNodeBase`


   Fields used to create a ShellFunctionNode.


   .. py:attribute:: shell_function_name
      :type:  str | None
      :value: None



   .. py:attribute:: shell_function_id
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



