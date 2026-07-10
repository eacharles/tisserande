from __future__ import annotations

import time
import traceback
from collections.abc import Callable
from typing import Any
from uuid import UUID

from ..models.types import ExecutionStatus, NodeType
from .backends import TrackingBackend
from .inspector import ArgumentInspector


class TrackingContext:
    """Manages the lifecycle of a single execution being tracked."""

    def __init__(self, backend: TrackingBackend) -> None:
        self._backend = backend
        self._execution_id: UUID | None = None
        self._function_node_id: UUID | None = None
        self._start_time: float = 0.0

    def start_execution(
        self,
        inspector: ArgumentInspector,
        args: tuple[Any, ...],
        kwargs: dict[str, Any],
    ) -> None:
        """Create Execution + function node + input nodes + input edges."""
        self._start_time = time.time()

        self._execution_id = self._backend.create_execution(
            status=ExecutionStatus.RUNNING.value,
        )

        self._function_node_id = self._backend.create_node(
            type_=NodeType.PYTHON_FUNCTION.value,
            execution_id=self._execution_id,
            arg_name=None,
        )

        self._backend.update_execution(
            self._execution_id,
            function_node_id=self._function_node_id,
        )

        input_specs = inspector.build_input_specs(args, kwargs)
        for spec in input_specs:
            spec["execution_id"] = self._execution_id
            input_node_id = self._backend.create_node(**spec)
            self._backend.create_edge(
                from_id=input_node_id,
                to_id=self._function_node_id,
                execution_id=self._execution_id,
            )

    def finish_execution(
        self,
        inspector: ArgumentInspector,
        result: Any,
        exception: BaseException | None = None,
    ) -> None:
        """Create output nodes + output edges, update Execution with timing/status."""
        assert self._execution_id is not None
        assert self._function_node_id is not None

        elapsed = time.time() - self._start_time

        if exception is not None:
            self._backend.update_execution(
                self._execution_id,
                status=ExecutionStatus.FAILURE.value,
                duration_seconds=elapsed,
                error_message=str(exception),
                error_traceback=traceback.format_exc(),
            )
            return

        output_specs = inspector.build_output_specs(result)
        for spec in output_specs:
            spec["execution_id"] = self._execution_id
            output_node_id = self._backend.create_node(**spec)
            self._backend.create_edge(
                from_id=self._function_node_id,
                to_id=output_node_id,
                execution_id=self._execution_id,
            )

        self._backend.update_execution(
            self._execution_id,
            status=ExecutionStatus.SUCCESS.value,
            duration_seconds=elapsed,
        )
