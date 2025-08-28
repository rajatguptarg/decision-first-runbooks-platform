"""Runbook and decision tree models."""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .base import BaseDBModel, PyObjectId
from .enums import SeverityLevel
from .execution_environment import ExecutionEnvironment


class Command(BaseModel):
    """A single command to be executed in a runbook step."""

    command: str
    description: str
    timeout_seconds: int = 300
    expected_exit_codes: list[int] = Field(default_factory=lambda: [0])


class DecisionOption(BaseModel):
    """An option for a decision node."""

    description: str
    next_node_id: str


class DecisionNode(BaseModel):
    """A node in the decision tree that represents a decision point."""

    id: str
    type: Literal["decision"]
    question: str
    description: str
    options: list[DecisionOption]


class ActionNode(BaseModel):
    """A node in the decision tree that represents an action to be taken."""

    id: str
    type: Literal["action"]
    title: str
    description: str
    commands: list[Command]
    next_node_id: str | None = None


class DecisionTree(BaseModel):
    """The decision tree structure for a runbook."""

    root_node_id: str
    nodes: dict[str, DecisionNode | ActionNode]


class Runbook(BaseDBModel):
    """The main runbook model."""

    title: str
    description: str
    owner_id: PyObjectId
    severity: SeverityLevel
    execution_environment: ExecutionEnvironment
    decision_tree: DecisionTree
    version: int
    tags: list[str] = Field(default_factory=list)


class RunbookCreate(BaseModel):
    """Runbook creation model."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    title: str
    description: str
    owner_id: PyObjectId
    severity: SeverityLevel
    execution_environment: ExecutionEnvironment
    decision_tree: DecisionTree
    tags: list[str] = Field(default_factory=list)


class RunbookUpdate(BaseModel):
    """Runbook update model."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    title: str | None = None
    description: str | None = None
    severity: SeverityLevel | None = None
    execution_environment: ExecutionEnvironment | None = None
    decision_tree: DecisionTree | None = None
    tags: list[str] | None = None
