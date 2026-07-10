tisserande.models.execution
===========================

.. py:module:: tisserande.models.execution

.. autoapi-nested-parse::

   Pydantic models for execution records (one per tracked function call).



Classes
-------

.. autoapisummary::

   tisserande.models.execution.ExecutionBase
   tisserande.models.execution.ExecutionCreate
   tisserande.models.execution.Execution


Module Contents
---------------

.. py:class:: ExecutionBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for an execution record grouping nodes/edges from a single function call.


   .. py:attribute:: status
      :type:  tisserande.models.types.ExecutionStatus
      :value: None



   .. py:attribute:: start_time
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: end_time
      :type:  datetime.datetime | None
      :value: None



   .. py:attribute:: duration_seconds
      :type:  float | None
      :value: None



   .. py:attribute:: error_message
      :type:  str | None
      :value: None



   .. py:attribute:: error_traceback
      :type:  str | None
      :value: None



.. py:class:: ExecutionCreate(/, **data: Any)

   Bases: :py:obj:`ExecutionBase`


   Fields used to create an Execution.


   .. py:attribute:: function_node_id
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



