tisserande.db.nodes
===================

.. py:module:: tisserande.db.nodes

.. autoapi-nested-parse::

   ORM model for the Node table (single table for all node types).

   All node types (data files, config files, parameters, arrays, objects,
   python functions, member functions, shell functions) share this one table.
   Type-specific fields are nullable columns. This design simplifies graph
   queries since edges only reference one table.



Classes
-------

.. autoapisummary::

   tisserande.db.nodes.NodeTable


Module Contents
---------------

.. py:class:: NodeTable

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
      :type:  sqlalchemy.orm.Mapped[uuid.UUID]


   .. py:attribute:: type_
      :type:  sqlalchemy.orm.Mapped[str]


   .. py:attribute:: execution_id
      :type:  sqlalchemy.orm.Mapped[uuid.UUID | None]


   .. py:attribute:: path
      :type:  sqlalchemy.orm.Mapped[str | None]


   .. py:attribute:: config_data
      :type:  sqlalchemy.orm.Mapped[dict | None]


   .. py:attribute:: value_float
      :type:  sqlalchemy.orm.Mapped[float | None]


   .. py:attribute:: value_json
      :type:  sqlalchemy.orm.Mapped[dict | list | None]


   .. py:attribute:: arg_name
      :type:  sqlalchemy.orm.Mapped[str | None]


   .. py:attribute:: data_file_type_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: config_file_type_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: config_dict_type_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: parameter_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: array_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: class_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: python_function_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: member_function_id
      :type:  sqlalchemy.orm.Mapped[int | None]


   .. py:attribute:: shell_function_id
      :type:  sqlalchemy.orm.Mapped[int | None]


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



