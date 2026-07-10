tisserande.db_oper.execution
============================

.. py:module:: tisserande.db_oper.execution


Attributes
----------

.. autoapisummary::

   tisserande.db_oper.execution.execution


Classes
-------

.. autoapisummary::

   tisserande.db_oper.execution.ExecutionOperations


Module Contents
---------------

.. py:class:: ExecutionOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.execution.ExecutionTable`\ , :py:obj:`tisserande.models.Execution`\ , :py:obj:`tisserande.models.ExecutionCreate`\ ]


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


.. py:data:: execution

