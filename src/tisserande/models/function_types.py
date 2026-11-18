"""Pydantic models for function type tables (PythonFunction, MemberFunction, ShellFunction)."""

from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


# Python Fuction

class PythonFunctionMixin:
    """Mixin class for a FunctionNodeTemplate that is a python function."""

    module_: str = Field(..., description="Module where it lives")


class PythonFunctionCreate(FunctionNodeTemplateCreate, PythonFunctionMixin):
    """Fields used to create a PythonFunction that are not in the DB."""


class PythonFunction(FunctionNodeTemplate, PythonFunctionMixin):
    """PythonFunction response model."""


class PythonFunctionCallMixin:
    """Mixin class for a FunctionNode that is a call to a python function."""

    
class PythonFunctionCallCreate(FunctionNodeCreate, PythonFunctionCallMixin):
    """Fields used to create a PythonFunctionCall that are not in the DB."""


class PythonFunctionCall(FunctionNode, PythonFunctionCallMixin):
    """PythonFunctionCall response model."""


# Member Fuction    

class MemberFunctionMixin:
    """Mixin class for a FunctionNodeTemplate that is a member function."""

    name: str = Field(..., description="Name of the function")


class MemberFunctionCreate(FunctionNodeTemplateCreate, MemberFunctionMixin):
    """Fields used to create a MemberFunction that are not in the DB."""


class MemberFunction(FunctionNodeTemplate, MemberFunctionMixin):
    """MemberFunction response model."""

    class_id: int = Field(..., description="Foreign key into class table")


class MemberFunctionCallMixin:
    """Mixin class for a FunctionNodeTemplate that is a call to a member function."""


class MemberFunctionCallCreate(FunctionNodeCreate, MemberFunctionCallMixin):
    """Fields used to create a MemberFunction that are not in the DB."""


class MemberFunctionCall(FunctionNode, MemberFunctionCallMixin):
    """MemberFunctionCal response model."""


    
# Shell function    

class ShellFunctionMixin:
    """Mixin class for a FunctionNodeTemplate that is a shell script."""


class ShellFunctionCreate(FunctionNodeTemplateCreate, ShellFunctionMixin):
    """Fields used to create a ShellFunction that are not in the DB."""


class ShellFunction(FunctionNodeTemplateCreate, ShellFunctionMixin):
    """ShellFunction response model."""


class ShellFunctionCallMixin:
    """Mixin class for a FunctionNode that is a shell script."""


class ShellFunctionCallCreate(FunctionNodeCreate, ShellFunctionCallMixin):
    """Fields used to create a ShellFunction that are not in the DB."""


class ShellFunctionCall(FunctionNodeCreate, ShellFunctionCallMixin):
    """ShellFunctionCall response model."""
