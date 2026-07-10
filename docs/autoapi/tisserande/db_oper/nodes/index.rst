tisserande.db_oper.nodes
========================

.. py:module:: tisserande.db_oper.nodes


Attributes
----------

.. autoapisummary::

   tisserande.db_oper.nodes.node


Classes
-------

.. autoapisummary::

   tisserande.db_oper.nodes.NodeOperations


Module Contents
---------------

.. py:class:: NodeOperations(context: TableContext[T, ResponseT, CreateT])

   Bases: :py:obj:`macon.db_oper.base.TableOperations`\ [\ :py:obj:`tisserande.db.nodes.NodeTable`\ , :py:obj:`tisserande.models.Node`\ , :py:obj:`tisserande.models.NodeCreate`\ ]


   Operations for the Node table with type-dependent FK resolution.


   .. py:method:: get_create_kwargs(session: sqlalchemy.ext.asyncio.AsyncSession, **kwargs: Any) -> dict[str, Any]
      :async:


      Prepare kwargs for creating an instance.



.. py:data:: node

