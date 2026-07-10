tisserande.db_oper.function_types
=================================

.. py:module:: tisserande.db_oper.function_types


Attributes
----------

.. autoapisummary::

   tisserande.db_oper.function_types.python_function
   tisserande.db_oper.function_types.member_function
   tisserande.db_oper.function_types.shell_function


Classes
-------

.. autoapisummary::

   tisserande.db_oper.function_types.PythonFunctionOperations
   tisserande.db_oper.function_types.MemberFunctionOperations
   tisserande.db_oper.function_types.ShellFunctionOperations


Module Contents
---------------

.. py:class:: PythonFunctionOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.function_types.PythonFunctionTable`\ , :py:obj:`tisserande.models.PythonFunction`\ , :py:obj:`tisserande.models.PythonFunctionCreate`\ ]


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


.. py:class:: MemberFunctionOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.function_types.MemberFunctionTable`\ , :py:obj:`tisserande.models.MemberFunction`\ , :py:obj:`tisserande.models.MemberFunctionCreate`\ ]


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


   .. py:method:: get_create_kwargs(session: sqlalchemy.ext.asyncio.AsyncSession, class_id: macon.common.RowId | None = None, class_name: str | None = None, **kwargs: Any) -> dict[str, Any]
      :async:


      Prepare kwargs for creating an instance.



.. py:class:: ShellFunctionOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.function_types.ShellFunctionTable`\ , :py:obj:`tisserande.models.ShellFunction`\ , :py:obj:`tisserande.models.ShellFunctionCreate`\ ]


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


.. py:data:: python_function

.. py:data:: member_function

.. py:data:: shell_function

