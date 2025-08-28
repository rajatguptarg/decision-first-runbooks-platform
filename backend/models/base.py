"""Base model for database documents."""
from datetime import UTC, datetime

from pydantic import BaseModel, ConfigDict, Field


class BaseDBModel(BaseModel):
    """Base model for database documents."""

    model_config = ConfigDict(populate_by_name=True)

    id: str | None = Field(alias="_id", default=None)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
