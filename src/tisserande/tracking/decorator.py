"""Tracking decorators: @track, @track_async, and track_shell().

These are the primary user-facing API for automatic provenance capture.
"""

from __future__ import annotations

import subprocess
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, overload

from .backends import LocalSyncBackend, TrackingBackend
from .context import TrackingContext
from .inspector import ArgumentInspector

F = TypeVar("F", bound=Callable[..., Any])

_default_backend: TrackingBackend | None = None


def configure(
    *,
    backend: TrackingBackend | None = None,
    db_url: str | None = None,
) -> None:
    """Configure the tracking system.

    Must be called before @track is used (unless a backend is passed directly
    to the decorator). If neither backend nor db_url is provided, creates a
    LocalSyncBackend with the default DB URL from config.
    """
    global _default_backend

    if backend is not None:
        _default_backend = backend
        return

    from ..config import get_config
    from ..db.base import Base, init_db

    url = db_url or get_config().db.url
    init_db(url)

    import asyncio

    from ..db.base import get_session

    async def _create_tables() -> None:
        async with get_session() as session:
            conn = await session.connection()
            await conn.run_sync(Base.metadata.create_all)

    asyncio.run(_create_tables())
    _default_backend = LocalSyncBackend()


def get_backend() -> TrackingBackend | None:
    """Get the currently configured backend."""
    return _default_backend


def reset() -> None:
    """Reset the tracking system, clearing the configured backend."""
    global _default_backend
    _default_backend = None


@overload
def track(func: F) -> F: ...


@overload
def track(
    *,
    backend: TrackingBackend | None = None,
    track_inputs: bool = True,
    track_outputs: bool = True,
) -> Callable[[F], F]: ...


def track(
    func: F | None = None,
    *,
    backend: TrackingBackend | None = None,
    track_inputs: bool = True,
    track_outputs: bool = True,
) -> F | Callable[[F], F]:
    """Decorator to track execution provenance of a sync function.

    Can be used with or without arguments:
        @track
        def my_func(...): ...

        @track(track_outputs=False)
        def my_func(...): ...
    """

    def decorator(fn: F) -> F:
        inspector = ArgumentInspector(fn)

        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            be = backend or _default_backend
            if be is None:
                return fn(*args, **kwargs)

            ctx = TrackingContext(be)

            if track_inputs:
                ctx.start_execution(inspector, args, kwargs)
            else:
                ctx.start_execution(inspector, (), {})

            try:
                result = fn(*args, **kwargs)
            except Exception as exc:
                ctx.finish_execution(inspector, None, exception=exc)
                raise

            if track_outputs:
                ctx.finish_execution(inspector, result)
            else:
                ctx.finish_execution(inspector, None)

            return result

        return wrapper  # type: ignore[return-value]

    if func is not None:
        return decorator(func)
    return decorator


@overload
def track_async(func: F) -> F: ...


@overload
def track_async(
    *,
    backend: TrackingBackend | None = None,
    track_inputs: bool = True,
    track_outputs: bool = True,
) -> Callable[[F], F]: ...


def track_async(
    func: F | None = None,
    *,
    backend: TrackingBackend | None = None,
    track_inputs: bool = True,
    track_outputs: bool = True,
) -> F | Callable[[F], F]:
    """Decorator to track execution provenance of an async function."""

    def decorator(fn: F) -> F:
        inspector = ArgumentInspector(fn)

        @wraps(fn)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            be = backend or _default_backend
            if be is None:
                return await fn(*args, **kwargs)

            ctx = TrackingContext(be)

            if track_inputs:
                ctx.start_execution(inspector, args, kwargs)
            else:
                ctx.start_execution(inspector, (), {})

            try:
                result = await fn(*args, **kwargs)
            except Exception as exc:
                ctx.finish_execution(inspector, None, exception=exc)
                raise

            if track_outputs:
                ctx.finish_execution(inspector, result)
            else:
                ctx.finish_execution(inspector, None)

            return result

        return wrapper  # type: ignore[return-value]

    if func is not None:
        return decorator(func)
    return decorator


def track_shell(
    command: str | list[str],
    *,
    inputs: dict[str, Any] | None = None,
    outputs: dict[str, Any] | None = None,
    backend: TrackingBackend | None = None,
) -> subprocess.CompletedProcess[str]:
    """Execute and track a shell command.

    Parameters
    ----------
    command
        Shell command to execute
    inputs
        Dict mapping arg names to values (tracked as input data nodes)
    outputs
        Dict mapping output names to values (tracked as output data nodes)
    """
    from datetime import UTC, datetime

    from ..models.types import ExecutionStatus, NodeType

    be = backend or _default_backend

    if be is None:
        return subprocess.run(
            command,
            shell=isinstance(command, str),
            capture_output=True,
            text=True,
            check=False,
        )

    from .inspector import _classify_by_value, build_node_kwargs

    function_node_id = be.create_node(
        node_type=NodeType.SHELL_FUNCTION_CALL,
        status=ExecutionStatus.RUNNING,
        start_time=datetime.now(UTC),
    )

    if inputs:
        for _name, value in inputs.items():
            node_type = _classify_by_value(value)
            kwargs = build_node_kwargs(node_type, value, "track_shell")
            input_node_id = be.create_node(**kwargs)
            be.create_edge(from_id=input_node_id, to_id=function_node_id)


    result = subprocess.run(
        command,
        shell=isinstance(command, str),
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        be.update_node(
            function_node_id,
            status=ExecutionStatus.FAILURE,
            end_time=datetime.now(UTC),
            exception_message=result.stderr or f"Exit code {result.returncode}",
        )
        return result

    if outputs:
        for _name, value in outputs.items():
            node_type = _classify_by_value(value)
            kwargs = build_node_kwargs(node_type, value, "track_shell")
            output_node_id = be.create_node(**kwargs)
            be.create_edge(from_id=function_node_id, to_id=output_node_id)

    be.update_node(function_node_id, status=ExecutionStatus.SUCCESS, end_time=datetime.now(UTC))
    return result
