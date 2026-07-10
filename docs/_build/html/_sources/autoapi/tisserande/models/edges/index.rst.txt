tisserande.models.edges
=======================

.. py:module:: tisserande.models.edges

.. autoapi-nested-parse::

   Pydantic models for provenance graph edges connecting nodes.



Classes
-------

.. autoapisummary::

   tisserande.models.edges.EdgeBase
   tisserande.models.edges.EdgeCreate
   tisserande.models.edges.Edge


Module Contents
---------------

.. py:class:: EdgeBase(/, **data: Any)

   Bases: :py:obj:`pydantic.BaseModel`


   Model for a graph edge connecting two nodes.


   .. py:attribute:: from_id
      :type:  uuid.UUID
      :value: None



   .. py:attribute:: to_id
      :type:  uuid.UUID
      :value: None



.. py:class:: EdgeCreate(/, **data: Any)

   Bases: :py:obj:`EdgeBase`


   Fields used to create an Edge.


   .. py:attribute:: execution_id
      :type:  uuid.UUID | None
      :value: None



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



