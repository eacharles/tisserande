"""Pydantic models for execution records (one per tracked function call)."""

from datetime import datetime
from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from .types import ExecutionStatus


class ExecutionBase(BaseModel):
    """Model for an execution record grouping nodes/edges from a single function call."""

    status: ExecutionStatus = Field(default=ExecutionStatus.PENDING, description="Execution status")
    start_time: datetime | None = Field(default=None, description="When execution started")
    end_time: datetime | None = Field(default=None, description="When execution ended")
    duration_seconds: float | None = Field(default=None, description="Duration in seconds")
    error_message: str | None = Field(default=None, description="Error message if failed")
    error_traceback: str | None = Field(default=None, description="Full traceback if failed")


class ExecutionCreate(ExecutionBase):
    """Fields used to create an Execution."""

    function_node_id: UUID | None = Field(default=None, description="The function node for this execution")


class Execution(ExecutionBase):
    """Execution response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = [
        "id_",
        "function_node_id",
        "status",
        "start_time",
        "duration_seconds",
    ]

    id_: UUID
    function_node_id: UUID | None = None
