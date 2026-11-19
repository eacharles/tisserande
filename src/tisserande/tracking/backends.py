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

    def create_node(self, **kwargs: Any) -> UUID: ...

    def update_node(self, node_id: UUID, **kwargs: Any) -> None: ...

    def create_edge(self, from_id: UUID, to_id: UUID) -> int: ...


class LocalSyncBackend:
    """Uses tisserande.local_sync to store provenance in the local DB."""

    def __init__(self) -> None:
        from ..local_sync import edge, node

        self._node_ops = node
        self._edge_ops = edge

    def create_node(self, **kwargs: Any) -> UUID:
        result = self._node_ops.create_row(**kwargs)
        return result.uid_

    def update_node(self, node_id: UUID, **kwargs: Any) -> None:
        kwargs = {k: v.value if isinstance(v, enum.Enum) else v for k, v in kwargs.items()}
        self._node_ops.update_row(node_id, **kwargs)

    def create_edge(self, from_id: UUID, to_id: UUID) -> int:
        result = self._edge_ops.create_row(from_id=from_id, to_id=to_id)
        return result.id_


class NullBackend:
    """Discards all provenance. Useful for testing or disabling tracking."""

    _counter = itertools.count(1)

    def create_node(self, **kwargs: Any) -> UUID:  # pylint: disable=unused-argument
        import uuid

        return uuid.uuid4()

    def update_node(self, node_id: UUID, **kwargs: Any) -> None:  # pylint: disable=unused-argument
        pass

    def create_edge(self, from_id: UUID, to_id: UUID) -> int:  # pylint: disable=unused-argument
        return next(NullBackend._counter)
