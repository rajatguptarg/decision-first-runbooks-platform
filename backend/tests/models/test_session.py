"""Unit tests for the Session and TimelineEvent models."""
from datetime import datetime

import pytest
from pydantic import ValidationError

from backend.models.enums import EventType, SessionStatus
from backend.models.session import Session, TimelineEvent


def test_timeline_event_creation():
    """Test successful TimelineEvent model creation."""
    event_data = {
        "session_id": "session123",
        "event_type": EventType.SESSION_STARTED,
        "user_id": "user123",
        "data": {"message": "Session has begun."},
    }
    event = TimelineEvent(**event_data)

    assert event.session_id == event_data["session_id"]
    assert event.event_type == event_data["event_type"]
    assert event.user_id == event_data["user_id"]
    assert event.data == event_data["data"]
    assert isinstance(event.timestamp, datetime)


def test_session_creation():
    """Test successful Session model creation."""
    session_data = {
        "runbook_id": "runbook123",
        "user_id": "user123",
        "status": SessionStatus.ACTIVE,
        "current_node_id": "node1",
        "execution_path": ["node0", "node1"],
        "container_id": "container123",
    }
    session = Session(**session_data)

    assert session.runbook_id == session_data["runbook_id"]
    assert session.user_id == session_data["user_id"]
    assert session.status == session_data["status"]
    assert session.current_node_id == session_data["current_node_id"]
    assert session.execution_path == session_data["execution_path"]
    assert session.container_id == session_data["container_id"]


def test_session_defaults():
    """Test that default values are set correctly for Session."""
    session = Session(
        runbook_id="runbook123",
        user_id="user123",
        status=SessionStatus.ACTIVE,
        current_node_id="node1",
    )
    assert session.execution_path == []
    assert session.container_id is None
    assert session.completed_at is None


def test_session_invalid_status():
    """Test that validation fails for an invalid status."""
    with pytest.raises(ValidationError):
        Session(
            runbook_id="runbook123",
            user_id="user123",
            status="invalid_status",
            current_node_id="node1",
        )
