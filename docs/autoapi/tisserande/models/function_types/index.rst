tisserande.models.function_types
================================

.. py:module:: tisserande.models.function_types

.. autoapi-nested-parse::

   Pydantic models for function type tables (PythonFunction, MemberFunction, ShellFunction).



Classes
-------

.. autoapisummary::

   tisserande.models.function_types.PythonFunctionBase
   tisserande.models.function_types.PythonFunctionCreate
   tisserande.models.function_types.PythonFunction
   tisserande.models.function_types.MemberFunctionBase
   tisserande.models.function_types.MemberFunctionCreate
   tisserande.models.function_types.MemberFunction
   tisserande.models.function_types.ShellFunctionBase
   tisserande.models.function_types.ShellFunctionCreate
   tisserande.models.function_types.ShellFunction


Module Contents
---------------

.. py:class:: PythonFunctionBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a python function.


   .. py:attribute:: name
      :type:  str
      :value: None



   .. py:attribute:: module_
      :type:  str
      :value: None



.. py:class:: PythonFunctionCreate(/, **data: Any)

   Bases: :py:obj:`PythonFunctionBase`


   Fields used to create a PythonFunction.


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



.. py:class:: MemberFunctionBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a member function.


   .. py:attribute:: name
      :type:  str
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



.. py:class:: ShellFunctionBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a shell function/script.


   .. py:attribute:: name
      :type:  str
      :value: None



.. py:class:: ShellFunctionCreate(/, **data: Any)

   Bases: :py:obj:`ShellFunctionBase`


   Fields used to create a ShellFunction.


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



