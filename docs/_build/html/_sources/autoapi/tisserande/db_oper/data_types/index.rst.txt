tisserande.db_oper.data_types
=============================

.. py:module:: tisserande.db_oper.data_types


Attributes
----------

.. autoapisummary::

   tisserande.db_oper.data_types.data_file_type
   tisserande.db_oper.data_types.config_file_type
   tisserande.db_oper.data_types.config_dict_type
   tisserande.db_oper.data_types.parameter
   tisserande.db_oper.data_types.array
   tisserande.db_oper.data_types.class_


Classes
-------

.. autoapisummary::

   tisserande.db_oper.data_types.DataFileTypeOperations
   tisserande.db_oper.data_types.ConfigFileTypeOperations
   tisserande.db_oper.data_types.ConfigDictTypeOperations
   tisserande.db_oper.data_types.ParameterOperations
   tisserande.db_oper.data_types.ArrayOperations
   tisserande.db_oper.data_types.ClassOperations


Module Contents
---------------

.. py:class:: DataFileTypeOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.DataFileTypeTable`\ , :py:obj:`tisserande.models.DataFileType`\ , :py:obj:`tisserande.models.DataFileTypeCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:class:: ConfigFileTypeOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigFileTypeTable`\ , :py:obj:`tisserande.models.ConfigFileType`\ , :py:obj:`tisserande.models.ConfigFileTypeCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:class:: ConfigDictTypeOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.ConfigDictTypeTable`\ , :py:obj:`tisserande.models.ConfigDictType`\ , :py:obj:`tisserande.models.ConfigDictTypeCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:class:: ParameterOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.ParameterTable`\ , :py:obj:`tisserande.models.Parameter`\ , :py:obj:`tisserande.models.ParameterCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:class:: ArrayOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.ArrayTable`\ , :py:obj:`tisserande.models.Array`\ , :py:obj:`tisserande.models.ArrayCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:class:: ClassOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.data_types.ClassTable`\ , :py:obj:`tisserande.models.Class`\ , :py:obj:`tisserande.models.ClassCreate`\ ]


   Base class for Table operations with full type safety.

   Provides common CRUD operations for database tables with validation,
   lifecycle hooks, and complete type safety across database models and
   their Pydantic representations.

   Type Parameters
   ---------------
   T : TypeVar, bound=Base
       Database model class (SQLAlchemy)
   ResponseT : TypeVar, bound=BaseModel
       Pydantic model class for responses
   CreateT : TypeVar, bound=BaseModel
       Pydantic model class for creation

   .. important::

      All methods that modify the database (create_row, create_rows, etc.)
      DO NOT commit transactions. The caller MUST manage transactions using
      `async with session.begin()` or explicit commit/rollback.
      
      All create methods DO add objects to the session and flush them to
      get database-generated values (like auto-increment IDs), but the
      transaction must still be committed by the caller.

   :param context: Shared configuration for this operation

   .. rubric:: Examples

   >>> from myapp.models import User, UserResponse, UserCreate
   >>> context = TableContext(
   ...     db_class=User,
   ...     response_class=UserResponse,
   ...     create_class=UserCreate,
   ...     class_string="user"
   ... )
   >>> ops = TableOperations(context)
   >>>
   >>> async with get_session() as session:
   ...     async with session.begin():
   ...         user = await ops.create_row(
   ...             session,
   ...             username="alice",
   ...             email="alice@example.com"
   ...         )
   ...         # user is type User (T)
   ...         pydantic_user = ops.to_pydantic(user)
   ...         # pydantic_user is type UserResponse (ResponseT)


.. py:data:: data_file_type

.. py:data:: config_file_type

.. py:data:: config_dict_type

.. py:data:: parameter

.. py:data:: array

.. py:data:: class_

