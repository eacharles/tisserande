"""Pluggable storage backends for provenance records.

The TrackingBackend protocol defines the interface; concrete implementations
include LocalSyncBackend (real DB) and NullBackend (no-op for testing).
"""

from __future__ import annotations

import enum
import itertools
from typing import Any, Protocol
from uuid import UUID


class TrackingBackend(Protocol):
    """Protocol for provenance storage backends."""

    def create_execution(self, **kwargs: Any) -> UUID: ...

    def update_execution(self, execution_id: UUID, **kwargs: Any) -> None: ...

    def create_node(self, **kwargs: Any) -> UUID: ...

    def create_edge(self, from_id: UUID, to_id: UUID, execution_id: UUID) -> int: ...


class LocalSyncBackend:
    """Uses tisserande.local_sync to store provenance in the local DB."""

    def __init__(self) -> None:
        from ..local_sync import edge, execution, node

        self._node_ops = node
        self._edge_ops = edge
        self._execution_ops = execution

    def create_execution(self, **kwargs: Any) -> UUID:
        result = self._execution_ops.create_row(**kwargs)
        return result.id_

    def update_execution(self, execution_id: UUID, **kwargs: Any) -> None:
        kwargs = {k: v.value if isinstance(v, enum.Enum) else v for k, v in kwargs.items()}
        self._execution_ops.update_row(execution_id, **kwargs)

    def create_node(self, **kwargs: Any) -> UUID:
        result = self._node_ops.create_row(**kwargs)
        return result.id_

    def create_edge(self, from_id: UUID, to_id: UUID, execution_id: UUID) -> int:
        result = self._edge_ops.create_row(from_id=from_id, to_id=to_id, execution_id=execution_id)
        return result.id_


class NullBackend:
    """Discards all provenance. Useful for testing or disabling tracking."""

    _counter = itertools.count(1)

    def create_execution(self, **kwargs: Any) -> UUID:  # pylint: disable=unused-argument
        import uuid

        return uuid.uuid4()

    def update_execution(self, execution_id: UUID, **kwargs: Any) -> None:  # pylint: disable=unused-argument
        pass

    def create_node(self, **kwargs: Any) -> UUID:  # pylint: disable=unused-argument
        import uuid

        return uuid.uuid4()

    def create_edge(self, from_id: UUID, to_id: UUID, execution_id: UUID) -> int:  # pylint: disable=unused-argument
        return next(NullBackend._counter)
