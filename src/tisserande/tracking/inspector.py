"""Argument introspection for classifying function inputs/outputs into node types."""

from __future__ import annotations

import inspect
import os
from collections.abc import Callable
from typing import Any, get_args, get_origin, get_type_hints

from ..models.types import NodeType
from .annotations import ANNOTATION_MAP


def _get_tisserande_annotation(type_hint: Any) -> str | None:
    """Extract tisserande annotation metadata from a type hint."""
    if get_origin(type_hint) is not None:
        args = get_args(type_hint)
        for arg in args:
            if isinstance(arg, str) and arg in ANNOTATION_MAP:
                return ANNOTATION_MAP[arg]
    return None


def _classify_by_value(value: Any) -> NodeType:
    """Classify a value into a NodeType using heuristics."""
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return NodeType.PARAMETER
    try:
        import numpy as np

        if isinstance(value, np.ndarray):
            return NodeType.ARRAY
    except ImportError:  # pragma: no cover
        pass
    if isinstance(value, str):
        if os.path.sep in value or value.endswith((".fits", ".hdf5", ".parquet", ".csv", ".npy")):
            return NodeType.DATA_FILE
        if value.endswith((".yaml", ".yml", ".json", ".toml", ".cfg", ".ini")):
            return NodeType.CONFIG_FILE
        return NodeType.PARAMETER
    if isinstance(value, dict):
        return NodeType.CONFIG_DICT
    if isinstance(value, (list, tuple)):
        if value and all(isinstance(v, (int, float)) for v in value):
            return NodeType.ARRAY
        return NodeType.OBJECT
    return NodeType.OBJECT


def build_node_kwargs(
    param_name: str,
    node_type: NodeType,
    value: Any,
) -> dict[str, Any]:
    """Build kwargs dict for creating a Node row."""
    kwargs: dict[str, Any] = {
        "type_": node_type,
        "arg_name": param_name,
    }

    if node_type == NodeType.DATA_FILE:
        kwargs["path"] = str(value)
    elif node_type == NodeType.CONFIG_FILE:
        kwargs["path"] = str(value)
    elif node_type == NodeType.CONFIG_DICT:
        kwargs["config_data"] = value
    elif node_type == NodeType.PARAMETER:
        kwargs["value_float"] = float(value) if isinstance(value, (int, float)) else None
        if kwargs["value_float"] is None:
            kwargs["value_json"] = value
    elif node_type == NodeType.ARRAY:
        kwargs["value_json"] = list(value) if not isinstance(value, list) else value
    elif node_type == NodeType.OBJECT:
        try:
            kwargs["value_json"] = value
        except (TypeError, ValueError):  # pragma: no cover
            kwargs["value_json"] = str(value)

    return kwargs


class ArgumentInspector:
    """Inspects function signatures and runtime args to create node specifications."""

    def __init__(self, func: Callable[..., Any]) -> None:
        self._func = func
        self._hints: dict[str, Any] = {}
        try:
            self._hints = get_type_hints(func, include_extras=True)
        except Exception:
            pass
        self._sig = inspect.signature(func)

    @property
    def function_name(self) -> str:
        return self._func.__name__

    @property
    def function_module(self) -> str:
        return self._func.__module__

    def classify_argument(self, param_name: str, value: Any) -> NodeType | None:
        """Determine NodeType for a parameter from annotation or value heuristics.

        Returns None if the argument is marked as Untracked.
        """
        hint = self._hints.get(param_name)
        if hint is not None:
            annotation = _get_tisserande_annotation(hint)
            if annotation == "untracked":
                return None
            if annotation is not None:
                return NodeType(annotation)

        return _classify_by_value(value)

    def classify_return(self, value: Any) -> NodeType | None:
        """Classify the return value."""
        hint = self._hints.get("return")
        if hint is not None:
            annotation = _get_tisserande_annotation(hint)
            if annotation == "untracked":
                return None
            if annotation is not None:
                return NodeType(annotation)

        return _classify_by_value(value)

    def build_node_kwargs(
        self,
        param_name: str,
        node_type: NodeType,
        value: Any,
    ) -> dict[str, Any]:
        """Build kwargs dict for creating a Node row."""
        return build_node_kwargs(param_name, node_type, value)

    def build_input_specs(
        self,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> list[dict[str, Any]]:
        """Build node creation specs for all tracked input arguments."""
        specs: list[dict[str, Any]] = []

        bound = self._sig.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            param = self._sig.parameters.get(name)
            if param and param.kind in (param.VAR_POSITIONAL, param.VAR_KEYWORD):
                continue

            node_type = self.classify_argument(name, value)
            if node_type is None:
                continue

            spec = self.build_node_kwargs(name, node_type, value)
            specs.append(spec)

        return specs

    def build_output_specs(self, result: Any) -> list[dict[str, Any]]:
        """Build node creation specs for the return value."""
        if result is None:
            return []

        if isinstance(result, tuple):
            specs = []
            for i, val in enumerate(result):
                node_type = _classify_by_value(val)
                spec = self.build_node_kwargs(f"return_{i}", node_type, val)
                specs.append(spec)
            return specs

        return_type = self.classify_return(result)
        if return_type is None:
            return []

        spec = self.build_node_kwargs("return", return_type, result)
        return [spec]
