"""Session and timeline models."""
from datetime import UTC, datetime
from typing import Any

from pydantic import Field

from .base import BaseDBModel
from .enums import EventType, SessionStatus


class TimelineEvent(BaseDBModel):
    """An event that occurred during a session."""

    session_id: str
    event_type: EventType
    timestamp: datetime = Field(default_factory=lambda: datetime.now(UTC))
    user_id: str
    data: dict[str, Any]


class Session(BaseDBModel):
    """An execution session for a runbook."""

    runbook_id: str
    user_id: str
    status: SessionStatus
    current_node_id: str
    execution_path: list[str] = Field(default_factory=list)
    container_id: str | None = None
    completed_at: datetime | None = None
