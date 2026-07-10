tisserande.models.data_types
============================

.. py:module:: tisserande.models.data_types

.. autoapi-nested-parse::

   Pydantic models for data-related type tables (DataFileType, ConfigFileType, etc.).



Classes
-------

.. autoapisummary::

   tisserande.models.data_types.DataFileTypeBase
   tisserande.models.data_types.DataFileTypeCreate
   tisserande.models.data_types.DataFileType
   tisserande.models.data_types.ConfigFileTypeBase
   tisserande.models.data_types.ConfigFileTypeCreate
   tisserande.models.data_types.ConfigFileType
   tisserande.models.data_types.ConfigDictTypeBase
   tisserande.models.data_types.ConfigDictTypeCreate
   tisserande.models.data_types.ConfigDictType
   tisserande.models.data_types.ParameterBase
   tisserande.models.data_types.ParameterCreate
   tisserande.models.data_types.Parameter
   tisserande.models.data_types.ArrayBase
   tisserande.models.data_types.ArrayCreate
   tisserande.models.data_types.Array
   tisserande.models.data_types.ClassBase
   tisserande.models.data_types.ClassCreate
   tisserande.models.data_types.Class


Module Contents
---------------

.. py:class:: DataFileTypeBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a type of file that contains data.


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: DataFileTypeCreate(/, **data: Any)

   Bases: :py:obj:`DataFileTypeBase`


   Fields used to create a DataFileType.


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



.. py:class:: ConfigFileTypeBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a type of file that contains configuration.


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: ConfigFileTypeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigFileTypeBase`


   Fields used to create a ConfigFileType.


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



.. py:class:: ConfigDictTypeBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a type of dict that contains configuration.


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: ConfigDictTypeCreate(/, **data: Any)

   Bases: :py:obj:`ConfigDictTypeBase`


   Fields used to create a ConfigDictType.


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



.. py:class:: ParameterBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a parameter definition.


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: ParameterCreate(/, **data: Any)

   Bases: :py:obj:`ParameterBase`


   Fields used to create a Parameter.


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



.. py:class:: ArrayBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for an array definition.


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: n_dim
      :type:  int
      :value: None



   .. py:attribute:: shape
      :type:  list[int]
      :value: None



.. py:class:: ArrayCreate(/, **data: Any)

   Bases: :py:obj:`ArrayBase`


   Fields used to create an Array.


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



.. py:class:: ClassBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a Python class definition.


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: module_
      :type:  str
      :value: None



.. py:class:: ClassCreate(/, **data: Any)

   Bases: :py:obj:`ClassBase`


   Fields used to create a Class.


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



