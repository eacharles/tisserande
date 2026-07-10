from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class TrackingConfiguration(BaseModel):
    """Configuration for the provenance tracking system."""

    enabled: bool = Field(
        default=True,
        description="Enable/disable provenance tracking globally",
    )

    backend: str = Field(
        default="local_sync",
        description="Default backend: local_sync, deferred, null",
    )

    auto_classify: bool = Field(
        default=True,
        description="Auto-classify argument types from annotations/heuristics",
    )


class DatabaseConfiguration(BaseModel):
    """Database configuration for tisserande."""

    url: str = Field(
        default="sqlite+aiosqlite:///tisserande.db",
        description="The URL for the tisserande provenance database",
    )

    echo: bool = Field(
        default=False,
        description="SQLAlchemy engine echo setting",
    )


class Configuration(BaseSettings):
    """Configuration for tisserande.

    Nested models may be consumed from environment variables named according to
    the pattern 'TISSERANDE__NESTED__FIELD'.
    """

    model_config = SettingsConfigDict(
        env_prefix="TISSERANDE__",
        env_nested_delimiter="__",
        nested_model_default_partial_update=True,
        case_sensitive=False,
        extra="ignore",
    )

    db: DatabaseConfiguration = DatabaseConfiguration()
    tracking: TrackingConfiguration = TrackingConfiguration()


config = Configuration()
