from typing import ClassVar

from pydantic import BaseModel, ConfigDict, Field


class PythonFunctionBase(BaseModel):
    """Model for a python function."""

    name: str = Field(..., description="Name of the function")
    module_: str = Field(..., description="Module where it lives")


class PythonFunctionCreate(PythonFunctionBase):
    """Fields used to create a PythonFunction."""


class PythonFunction(PythonFunctionBase):
    """PythonFunction response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "module_"]

    id_: int = Field(..., gt=0)


class MemberFunctionBase(BaseModel):
    """Model for a member function."""

    name: str = Field(..., description="Name of the function")


class MemberFunctionCreate(MemberFunctionBase):
    """Fields used to create a MemberFunction."""

    class_name: str | None = Field(default=None, description="Name of the owning class")
    class_id: int | None = Field(default=None, description="ID of the owning class")


class MemberFunction(MemberFunctionBase):
    """MemberFunction response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name", "class_id"]

    id_: int = Field(..., gt=0)
    class_id: int = Field(..., description="Foreign key into class table")


class ShellFunctionBase(BaseModel):
    """Model for a shell function/script."""

    name: str = Field(..., description="Name of the shell function")


class ShellFunctionCreate(ShellFunctionBase):
    """Fields used to create a ShellFunction."""


class ShellFunction(ShellFunctionBase):
    """ShellFunction response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "name"]

    id_: int = Field(..., gt=0)
