"""Pydantic models for function-type node templates and their runtime call instances.

Each function type is represented by two parallel sets of models:

* A *Template* pair (``...Create`` / ``...``) — reusable type definitions
  stored once in the NodeTemplate table (e.g. one record per unique Python
  function).
* A *Call* pair (``...CallCreate`` / ``...Call``) — runtime node records stored
  in the Node table, one per actual invocation.

Both sets follow the ``Base → Create → Response`` pattern established in
``base.py`` and use a plain mixin class to supply type-specific fields and
lock the ``node_template_type`` / ``node_type`` discriminator to a ``Literal``.
"""

from typing import Any, Literal
from uuid import UUID

from pydantic import Field

from .base import (
    FunctionNode,
    FunctionNodeCreate,
    FunctionNodeTemplate,
    FunctionNodeTemplateCreate,
)
from .types import NodeTemplateType, NodeType


# ---------------------------------------------------------------------------
# Python Function
# ---------------------------------------------------------------------------


class PythonFunctionMixin:
    """Mixin for a FunctionNodeTemplate that describes a Python function.

    ``module_`` identifies where the function lives so it can be imported
    programmatically.  The trailing underscore avoids shadowing Python's
    built-in ``module``.  Together with ``name`` from the base template, the
    fully-qualified function reference is ``module_ + "." + name``.

    ``is_async`` records whether the function is a coroutine, which is
    relevant when reasoning about parallelism in the provenance graph.
    """

    node_template_type: Literal[NodeTemplateType.PYTHON_FUNCTION] = NodeTemplateType.PYTHON_FUNCTION
    module_: str = Field(
        ...,
        description="Fully-qualified module where this function is defined (e.g. 'mypackage.pipeline').",
    )
    is_async: bool = Field(
        default=False, description="True if this function is a coroutine (defined with async def)."
    )


class PythonFunctionCreate(FunctionNodeTemplateCreate, PythonFunctionMixin):
    """Creation model for a PythonFunction template."""


class PythonFunction(FunctionNodeTemplate, PythonFunctionMixin):
    """Response model for a PythonFunction template."""


class PythonFunctionCallMixin:
    """Mixin for a FunctionNode that records a single call to a Python function.

    ``args_json`` and ``kwargs_json`` capture the positional and keyword
    arguments passed to the call in JSON-serialisable form, enabling
    reproduction of the exact call from the provenance record.

    ``return_value_json`` stores simple scalar or dict return values inline;
    complex return values are captured as separate output data nodes via edges.

    ``source_hash`` is a hash of the function's source code at the time of
    the call.  It lets you detect when two executions used different versions
    of the same function even if the template name and version were unchanged.
    """

    node_type: Literal[NodeType.PYTHON_FUNCTION_CALL] = NodeType.PYTHON_FUNCTION_CALL
    args_json: Any | None = Field(
        default=None,
        description="Positional arguments passed to this call, in JSON-serialisable form.",
    )
    kwargs_json: Any | None = Field(
        default=None,
        description="Keyword arguments passed to this call, in JSON-serialisable form.",
    )
    return_value_json: Any | None = Field(
        default=None, description="Return value of this call when it is a simple scalar or dict."
    )
    source_hash: str | None = Field(
        default=None, description="Hash of the function's source code at the time of the call."
    )


class PythonFunctionCallCreate(FunctionNodeCreate, PythonFunctionCallMixin):
    """Creation model for a PythonFunctionCall node."""


class PythonFunctionCall(FunctionNode, PythonFunctionCallMixin):
    """Response model for a PythonFunctionCall node."""


# ---------------------------------------------------------------------------
# Member Function (Python class method)
# ---------------------------------------------------------------------------


class MemberFunctionMixin:
    """Mixin for a FunctionNodeTemplate that describes a Python class method.

    ``name`` is the method name within the class identified by ``class_id``
    on the response model.  ``is_async`` records whether the method is a
    coroutine.
    """

    node_template_type: Literal[NodeTemplateType.MEMBER_FUNCTION] = NodeTemplateType.MEMBER_FUNCTION
    name: str = Field(..., description="Name of the method (without the class prefix).")
    is_async: bool = Field(
        default=False, description="True if this method is a coroutine (defined with async def)."
    )


class MemberFunctionCreate(FunctionNodeTemplateCreate, MemberFunctionMixin):
    """Creation model for a MemberFunction template."""


class MemberFunction(FunctionNodeTemplate, MemberFunctionMixin):
    """Response model for a MemberFunction template."""

    class_id: int = Field(..., description="Foreign key into the Class template table that owns this method.")


class MemberFunctionCallMixin:
    """Mixin for a FunctionNode that records a single call to a class method.

    ``instance_node_id`` is a foreign key to the ``ClassInstance`` node that
    was ``self`` for this call.  Without it, the graph cannot distinguish
    which object the method was invoked on.

    ``args_json``, ``kwargs_json``, ``return_value_json``, and ``source_hash``
    have the same semantics as on ``PythonFunctionCallMixin``.
    """

    node_type: Literal[NodeType.MEMBER_FUNCTION_CALL] = NodeType.MEMBER_FUNCTION_CALL
    instance_node_id: UUID | None = Field(
        default=None,
        description="UUID of the ClassInstance node that was 'self' for this call.",
    )
    args_json: Any | None = Field(
        default=None,
        description="Positional arguments passed to this call, in JSON-serialisable form.",
    )
    kwargs_json: Any | None = Field(
        default=None,
        description="Keyword arguments passed to this call, in JSON-serialisable form.",
    )
    return_value_json: Any | None = Field(
        default=None, description="Return value of this call when it is a simple scalar or dict."
    )
    source_hash: str | None = Field(
        default=None, description="Hash of the method's source code at the time of the call."
    )


class MemberFunctionCallCreate(FunctionNodeCreate, MemberFunctionCallMixin):
    """Creation model for a MemberFunctionCall node."""


class MemberFunctionCall(FunctionNode, MemberFunctionCallMixin):
    """Response model for a MemberFunctionCall node."""


# ---------------------------------------------------------------------------
# Shell Function
# ---------------------------------------------------------------------------


class ShellFunctionMixin:
    """Mixin for a FunctionNodeTemplate that describes a shell script.

    ``script_path`` points to the script file on disk.  ``interpreter``
    records the shell or runtime used to execute it (e.g. ``"bash"``,
    ``"zsh"``, ``"python"``).
    """

    node_template_type: Literal[NodeTemplateType.SHELL_FUNCTION] = NodeTemplateType.SHELL_FUNCTION
    script_path: str | None = Field(default=None, description="Path to the shell script file.")
    interpreter: str | None = Field(
        default=None,
        description="Interpreter used to run the script (e.g. 'bash', 'zsh', 'python').",
    )


class ShellFunctionCreate(FunctionNodeTemplateCreate, ShellFunctionMixin):
    """Creation model for a ShellFunction template."""


class ShellFunction(FunctionNodeTemplate, ShellFunctionMixin):
    """Response model for a ShellFunction template."""


class ShellFunctionCallMixin:
    """Mixin for a FunctionNode that records a single shell script invocation.

    ``command`` is the full command string that was executed.  ``return_code``
    is the process exit code (0 conventionally indicates success).  ``stdout``
    and ``stderr`` capture the process output, truncated if necessary.
    ``working_dir`` records the working directory at the time of invocation so
    relative paths in the command can be resolved.
    """

    node_type: Literal[NodeType.SHELL_FUNCTION_CALL] = NodeType.SHELL_FUNCTION_CALL
    command: str | None = Field(default=None, description="Full command string that was executed.")
    return_code: int | None = Field(
        default=None, description="Process exit code (0 indicates success by convention)."
    )
    stdout: str | None = Field(default=None, description="Captured standard output, truncated if necessary.")
    stderr: str | None = Field(default=None, description="Captured standard error, truncated if necessary.")
    working_dir: str | None = Field(default=None, description="Working directory at the time of invocation.")


class ShellFunctionCallCreate(FunctionNodeCreate, ShellFunctionCallMixin):
    """Creation model for a ShellFunctionCall node."""


class ShellFunctionCall(FunctionNode, ShellFunctionCallMixin):
    """Response model for a ShellFunctionCall node."""
