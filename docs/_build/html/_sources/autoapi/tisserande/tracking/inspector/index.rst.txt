tisserande.tracking.inspector
=============================

.. py:module:: tisserande.tracking.inspector

.. autoapi-nested-parse::

   Argument introspection for classifying function inputs/outputs into node types.



Classes
-------

.. autoapisummary::

   tisserande.tracking.inspector.ArgumentInspector


Module Contents
---------------

.. py:class:: ArgumentInspector(func: collections.abc.Callable[Ellipsis, Any])

   Inspects function signatures and runtime args to create node specifications.


   .. py:property:: function_name
      :type: str



   .. py:property:: function_module
      :type: str



   .. py:method:: classify_argument(param_name: str, value: Any) -> tisserande.models.types.NodeType | None

      Determine NodeType for a parameter from annotation or value heuristics.

      Returns None if the argument is marked as Untracked.



   .. py:method:: classify_return(value: Any) -> tisserande.models.types.NodeType | None

      Classify the return value.



   .. py:method:: build_node_kwargs(param_name: str, node_type: tisserande.models.types.NodeType, value: Any) -> dict[str, Any]

      Build kwargs dict for creating a Node row.



   .. py:method:: build_input_specs(args: tuple[Any, Ellipsis], kwargs: dict[str, Any]) -> list[dict[str, Any]]

      Build node creation specs for all tracked input arguments.



   .. py:method:: build_output_specs(result: Any) -> list[dict[str, Any]]

      Build node creation specs for the return value.



