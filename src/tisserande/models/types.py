"""Enumerations for node template types, node types, and execution status.

``NodeTemplateType`` and ``NodeType`` are discriminators used for
joined-table inheritance in the database and for Pydantic ``Literal``
discriminators in the model hierarchy.  The two enums are in bijection:
``TEMPLATE_TO_NODE_DICT`` and ``NODE_TO_TEMPLATE_DICT`` map between them.

``ExecutionStatus`` tracks the lifecycle of a function call or graph run.
"""

import enum


class NodeTemplateType(enum.Enum):
    """Discriminator for the NodeTemplate table."""

    DATA_FILE_TYPE = "data_file_type"
    CONFIG_FILE_TYPE = "config_file_type"
    CONFIG_DICT_TYPE = "config_dict_type"
    PARAMETER_TYPE = "parameter_type"
    ARRAY_TYPE = "array_type"
    CLASS_TYPE = "class_type"
    PYTHON_FUNCTION = "python_function"
    MEMBER_FUNCTION = "member_function"
    SHELL_FUNCTION = "shell_function"

    @property
    def is_data_template(self) -> bool:
        """True if this template type describes a data node."""
        return self in _DATA_TEMPLATE_TYPES

    @property
    def is_function_template(self) -> bool:
        """True if this template type describes a function node."""
        return self in _FUNCTION_TEMPLATE_TYPES


class NodeType(enum.Enum):
    """Discriminator for the Node table."""

    DATA_FILE = "data_file"
    CONFIG_FILE = "config_file"
    CONFIG_DICT = "config_dict"
    PARAMETER = "parameter"
    ARRAY = "array"
    CLASS_INSTANCE = "class_instance"
    PYTHON_FUNCTION_CALL = "python_function_call"
    MEMBER_FUNCTION_CALL = "member_function_call"
    SHELL_FUNCTION_CALL = "shell_function_call"

    @property
    def is_data(self) -> bool:
        """True if this node type represents a data node."""
        return self in _DATA_TYPES

    @property
    def is_function(self) -> bool:
        """True if this node type represents a function call node."""
        return self in _FUNCTION_TYPES


class ExecutionStatus(enum.Enum):
    """Lifecycle states for a tracked execution (function call or graph run)."""

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILURE = "failure"


_DATA_TEMPLATE_TYPES = frozenset(
    {
        NodeTemplateType.DATA_FILE_TYPE,
        NodeTemplateType.CONFIG_FILE_TYPE,
        NodeTemplateType.CONFIG_DICT_TYPE,
        NodeTemplateType.PARAMETER_TYPE,
        NodeTemplateType.ARRAY_TYPE,
        NodeTemplateType.CLASS_TYPE,
    }
)

_FUNCTION_TEMPLATE_TYPES = frozenset(
    {
        NodeTemplateType.PYTHON_FUNCTION,
        NodeTemplateType.MEMBER_FUNCTION,
        NodeTemplateType.SHELL_FUNCTION,
    }
)

_DATA_TYPES = frozenset(
    {
        NodeType.DATA_FILE,
        NodeType.CONFIG_FILE,
        NodeType.CONFIG_DICT,
        NodeType.PARAMETER,
        NodeType.ARRAY,
        NodeType.CLASS_INSTANCE,
    }
)

_FUNCTION_TYPES = frozenset(
    {
        NodeType.PYTHON_FUNCTION_CALL,
        NodeType.MEMBER_FUNCTION_CALL,
        NodeType.SHELL_FUNCTION_CALL,
    }
)

TEMPLATE_TO_NODE_DICT: dict[NodeTemplateType, NodeType] = {
    NodeTemplateType.DATA_FILE_TYPE: NodeType.DATA_FILE,
    NodeTemplateType.CONFIG_FILE_TYPE: NodeType.CONFIG_FILE,
    NodeTemplateType.CONFIG_DICT_TYPE: NodeType.CONFIG_DICT,
    NodeTemplateType.PARAMETER_TYPE: NodeType.PARAMETER,
    NodeTemplateType.ARRAY_TYPE: NodeType.ARRAY,
    NodeTemplateType.CLASS_TYPE: NodeType.CLASS_INSTANCE,
    NodeTemplateType.PYTHON_FUNCTION: NodeType.PYTHON_FUNCTION_CALL,
    NodeTemplateType.MEMBER_FUNCTION: NodeType.MEMBER_FUNCTION_CALL,
    NodeTemplateType.SHELL_FUNCTION: NodeType.SHELL_FUNCTION_CALL,
}

NODE_TO_TEMPLATE_DICT: dict[NodeType, NodeTemplateType] = {
    val: key for key, val in TEMPLATE_TO_NODE_DICT.items()
}
