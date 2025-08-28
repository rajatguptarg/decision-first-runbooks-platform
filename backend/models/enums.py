"""Enums for data models."""
from enum import Enum


class UserRole(str, Enum):
    """User roles in the system."""

    VIEWER = "viewer"
    EDITOR = "editor"
    ADMIN = "admin"


class SessionStatus(str, Enum):
    """Status of an execution session."""

    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    FAILED = "failed"


class EventType(str, Enum):
    """Type of event in a session timeline."""

    SESSION_STARTED = "session_started"
    DECISION_MADE = "decision_made"
    ACTION_EXECUTED = "action_executed"
    COMMAND_RUN = "command_run"
    SESSION_PAUSED = "session_paused"
    SESSION_COMPLETED = "session_completed"


class SeverityLevel(str, Enum):
    """Severity level of a runbook."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"
