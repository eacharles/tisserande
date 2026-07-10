from typing import Annotated, TypeVar

T = TypeVar("T")

DataFile = Annotated[T, "tisserande:data_file"]
ConfigFile = Annotated[T, "tisserande:config_file"]
ConfigDict = Annotated[T, "tisserande:config_dict"]
Param = Annotated[T, "tisserande:parameter"]
ArrayArg = Annotated[T, "tisserande:array"]
ObjectArg = Annotated[T, "tisserande:object"]
Untracked = Annotated[T, "tisserande:untracked"]

ANNOTATION_MAP: dict[str, str] = {
    "tisserande:data_file": "data_file",
    "tisserande:config_file": "config_file",
    "tisserande:config_dict": "config_dict",
    "tisserande:parameter": "parameter",
    "tisserande:array": "array",
    "tisserande:object": "object",
    "tisserande:untracked": "untracked",
}
