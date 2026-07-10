import enum


class NodeType(enum.Enum):

    DATA_FILE = "data_file"
    CONFIG_FILE = "config_file"
    CONFIG_DICT = "config_dict"
    PARAMETER = "parameter"
    ARRAY = "array"
    OBJECT = "object"
    PYTHON_FUNCTION = "python_function"
    MEMBER_FUNCTION = "member_function"
    SHELL_FUNCTION = "shell_function"

    @property
    def is_data(self) -> bool:
        return self in _DATA_TYPES

    @property
    def is_logic(self) -> bool:
        return self in _LOGIC_TYPES


class ExecutionStatus(enum.Enum):

    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILURE = "failure"


_DATA_TYPES = frozenset({
    NodeType.DATA_FILE,
    NodeType.CONFIG_FILE,
    NodeType.CONFIG_DICT,
    NodeType.PARAMETER,
    NodeType.ARRAY,
    NodeType.OBJECT,
})

_LOGIC_TYPES = frozenset({
    NodeType.PYTHON_FUNCTION,
    NodeType.MEMBER_FUNCTION,
    NodeType.SHELL_FUNCTION,
})
