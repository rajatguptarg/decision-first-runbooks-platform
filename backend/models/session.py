"""Session and timeline models."""
from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from .base import BaseDBModel, PyObjectId
from .enums import EventType, SessionStatus


class TimelineEvent(BaseDBModel):
    """An event that occurred during a session."""

    session_id: PyObjectId
    event_type: EventType
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    user_id: PyObjectId
    data: dict[str, Any]


class Session(BaseDBModel):
    """An execution session for a runbook."""

    runbook_id: PyObjectId
    user_id: PyObjectId
    status: SessionStatus
    current_node_id: str
    execution_path: list[str] = Field(default_factory=list)
    container_id: str | None = None
    completed_at: datetime | None = None


class SessionCreate(BaseModel):
    """Session creation model."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    runbook_id: PyObjectId
    user_id: PyObjectId
    status: SessionStatus
    current_node_id: str


class SessionUpdate(BaseModel):
    """Session update model."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    status: SessionStatus | None = None
    current_node_id: str | None = None
    execution_path: list[str] | None = None
    container_id: str | None = None
    completed_at: datetime | None = None
