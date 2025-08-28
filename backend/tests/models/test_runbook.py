"""Unit tests for the Runbook model."""
import pytest
from bson import ObjectId
from pydantic import ValidationError

from backend.models.enums import SeverityLevel
from backend.models.execution_environment import ExecutionEnvironment
from backend.models.runbook import (
    ActionNode,
    Command,
    DecisionNode,
    DecisionTree,
    Runbook,
)


@pytest.fixture
def sample_execution_environment():
    """Return a sample ExecutionEnvironment for testing."""
    return ExecutionEnvironment(name="test-env", base_image="ubuntu:latest")


@pytest.fixture
def sample_decision_tree():
    """Return a sample DecisionTree for testing."""
    return {
        "root_node_id": "node1",
        "nodes": {
            "node1": {
                "id": "node1",
                "type": "decision",
                "question": "Is the service down?",
                "description": "Check the main dashboard.",
                "options": [
                    {"description": "Yes", "next_node_id": "node2"},
                    {"description": "No", "next_node_id": "node3"},
                ],
            },
            "node2": {
                "id": "node2",
                "type": "action",
                "title": "Restart the service",
                "description": "Use the restart script.",
                "commands": [
                    {
                        "command": "./restart.sh",
                        "description": "Restart script",
                    }
                ],
            },
            "node3": {
                "id": "node3",
                "type": "action",
                "title": "Check for latency",
                "description": "Look at the latency graphs.",
                "commands": [],
            },
        },
    }


def test_runbook_creation(sample_execution_environment, sample_decision_tree):
    """Test successful Runbook model creation."""
    runbook_data = {
        "title": "Service Down",
        "description": "A runbook for when the main service is down.",
        "owner_id": ObjectId(),
        "severity": SeverityLevel.CRITICAL,
        "execution_environment": sample_execution_environment,
        "decision_tree": sample_decision_tree,
        "version": 1,
        "tags": ["critical", "service-down"],
    }
    runbook = Runbook(**runbook_data)

    assert runbook.title == runbook_data["title"]
    assert runbook.owner_id == runbook_data["owner_id"]
    assert runbook.severity == SeverityLevel.CRITICAL
    assert runbook.version == 1
    assert runbook.tags == ["critical", "service-down"]
    assert isinstance(runbook.decision_tree, DecisionTree)
    assert isinstance(runbook.decision_tree.nodes["node1"], DecisionNode)
    assert isinstance(runbook.decision_tree.nodes["node2"], ActionNode)


def test_runbook_missing_required_fields(sample_execution_environment):
    """Test that validation fails for missing required fields."""
    with pytest.raises(ValidationError):
        Runbook(
            title="Incomplete Runbook",
            owner_id=ObjectId(),
            severity=SeverityLevel.LOW,
            execution_environment=sample_execution_environment,
        )


def test_decision_tree_invalid_node_type(sample_decision_tree):
    """Test that validation fails for an invalid node type in the decision tree."""
    sample_decision_tree["nodes"]["node1"]["type"] = "invalid_type"
    with pytest.raises(ValidationError):
        DecisionTree(**sample_decision_tree)


def test_action_node_defaults():
    """Test that default values are set correctly for ActionNode."""
    node = ActionNode(
        id="node1",
        type="action",
        title="Test Action",
        description="A test action.",
        commands=[],
    )
    assert node.next_node_id is None


def test_command_defaults():
    """Test that default values are set correctly for Command."""
    cmd = Command(command="echo 'hello'", description="Print hello")
    assert cmd.timeout_seconds == 300
    assert cmd.expected_exit_codes == [0]
