"""Pydantic models for CECI structural association tables.

CeciPipelineStageAssoc records which stages belong to a pipeline definition.
This is a schema-level relationship stored separately from the DAG.

File-stage connectivity (formerly CeciFileStageAssoc / CeciFileStageInstanceAssoc)
is now expressed as edges between CeciFileNodes and CeciStageNodes in the main
EdgeTable, using the existing from_id → to_id graph structure.
"""

from typing import ClassVar
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class CeciPipelineStageAssocBase(BaseModel):
    """Association between a pipeline definition and a schema-level stage node."""

    ceci_pipeline_id: int = Field(..., description="Foreign key into CeciPipeline table")
    ceci_stage_node_id: UUID = Field(..., description="Foreign key into the CeciStageNode (schema node)")


class CeciPipelineStageAssocCreate(CeciPipelineStageAssocBase):
    """Fields used to create a CeciPipelineStageAssoc."""


class CeciPipelineStageAssoc(CeciPipelineStageAssocBase):
    """CeciPipelineStageAssoc response model."""

    model_config = ConfigDict(from_attributes=True)
    col_names_for_table: ClassVar[list[str]] = ["id_", "ceci_pipeline_id", "ceci_stage_node_id"]

    id_: int = Field(..., gt=0)
