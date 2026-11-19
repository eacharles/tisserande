"""Execution context that orchestrates provenance recording for one function call."""

from __future__ import annotations

import traceback
from datetime import UTC, datetime
from typing import Any
from uuid import UUID

from ..models.types import ExecutionStatus, NodeType
from .backends import TrackingBackend
from .inspector import ArgumentInspector


class TrackingContext:
    """Manages the lifecycle of a single execution being tracked."""

    def __init__(self, backend: TrackingBackend) -> None:
        self._backend = backend
        self._function_node_id: UUID | None = None

    def start_execution(
        self,
        inspector: ArgumentInspector,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> None:
        """Create the function call node, then input nodes and input edges."""
        self._function_node_id = self._backend.create_node(
            node_type=NodeType.PYTHON_FUNCTION_CALL,
            status=ExecutionStatus.RUNNING,
            start_time=datetime.now(UTC),
        )

        input_specs = inspector.build_input_specs(args, kwargs)
        for spec in input_specs:
            input_node_id = self._backend.create_node(**spec)
            self._backend.create_edge(from_id=input_node_id, to_id=self._function_node_id)

    def finish_execution(
        self,
        inspector: ArgumentInspector,
        result: Any,
        exception: BaseException | None = None,
    ) -> None:
        """Create output nodes and edges, then update the function call node."""
        if self._function_node_id is None:
            raise RuntimeError("finish_execution called before start_execution")

        if exception is not None:
            self._backend.update_node(
                self._function_node_id,
                status=ExecutionStatus.FAILURE,
                end_time=datetime.now(UTC),
                exception_type=type(exception).__qualname__,
                exception_message=str(exception),
            )
            return

        output_specs = inspector.build_output_specs(result)
        for spec in output_specs:
            output_node_id = self._backend.create_node(**spec)
            self._backend.create_edge(from_id=self._function_node_id, to_id=output_node_id)

        self._backend.update_node(
            self._function_node_id,
            status=ExecutionStatus.SUCCESS,
            end_time=datetime.now(UTC),
        )
