tisserande.db.edges
===================

.. py:module:: tisserande.db.edges

.. autoapi-nested-parse::

   ORM model for the Edge table (directed links between nodes in the provenance DAG).



Classes
-------

.. autoapisummary::

   tisserande.db.edges.EdgeTable


Module Contents
---------------

.. py:class:: EdgeTable

   Bases: :py:obj:`tisserande.db.base.Base`


   Declarative base for all database models.

   Provides:
       - Schema assignment from configuration
       - Consistent constraint naming for migrations
       - Shared metadata for all models
       - Required interface for Pydantic integration
       - Lifecycle hooks for create, update, and delete operations

   Subclasses must implement the abstract methods for Pydantic model integration.
   Subclasses may override hook methods to add custom behavior at various points
   in the row lifecycle.


   .. py:attribute:: id_
      :type:  sqlalchemy.orm.Mapped[int]


   .. py:attribute:: from_id
      :type:  sqlalchemy.orm.Mapped[uuid.UUID]


   .. py:attribute:: to_id
      :type:  sqlalchemy.orm.Mapped[uuid.UUID]


   .. py:attribute:: execution_id
      :type:  sqlalchemy.orm.Mapped[uuid.UUID | None]


   .. py:method:: pydantic_create_class() -> type[pydantic.BaseModel]
      :classmethod:


      Pydantic model used to create rows in this table.

      This model defines the schema for input validation when creating new rows.
      It may differ from pydantic_model_class() if creation requires different
      fields than the full model representation.

      :returns: The Pydantic model class for row creation

      .. rubric:: Examples

      >>> class User(Base):
      ...     @classmethod
      ...     def pydantic_create_class(cls) -> type[BaseModel]:
      ...         return UserCreate  # Excludes id, created_at, etc.



   .. py:method:: pydantic_model_class() -> type[pydantic.BaseModel]
      :classmethod:


      Pydantic model class for this table.

      This model defines the complete schema for serialization and validation
      of existing rows, typically including all fields.

      :returns: The Pydantic model class for row serialization/validation

      .. rubric:: Examples

      >>> class User(Base):
      ...     @classmethod
      ...     def pydantic_model_class(cls) -> type[BaseModel]:
      ...         return UserModel  # Includes all fields



   .. py:method:: class_string() -> str
      :classmethod:


      Name to use for help functions and descriptions.

      Override this if you want a custom display name different from __name__.

      :returns: The class name for display purposes



