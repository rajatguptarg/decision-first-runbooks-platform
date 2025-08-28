"""Integration tests for the RunbookRepository."""
import pytest
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.enums import SeverityLevel
from backend.models.runbook import Runbook
from backend.repositories.runbook import RunbookRepository

pytestmark = pytest.mark.integration


@pytest.fixture
def sample_runbook_data():
    """Return a sample Runbook for testing."""
    return {
        "title": "Service Down",
        "description": "A runbook for when the main service is down.",
        "owner_id": ObjectId(),
        "severity": SeverityLevel.CRITICAL,
        "execution_environment": {"name": "test-env", "base_image": "ubuntu:latest"},
        "decision_tree": {
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
            },
        },
        "version": 1,
        "tags": ["critical", "service-down"],
    }


@pytest.mark.asyncio
async def test_create_runbook(test_db: AsyncIOMotorDatabase, sample_runbook_data):
    """Test creating a runbook."""
    runbook_repo = RunbookRepository(test_db)
    await runbook_repo.collection.delete_many({})

    runbook = Runbook(**sample_runbook_data)
    created_runbook = await runbook_repo.create(runbook)

    assert created_runbook is not None
    assert created_runbook.id is not None
    assert created_runbook.title == sample_runbook_data["title"]

    db_runbook = await runbook_repo.get(created_runbook.id)
    assert db_runbook is not None
    assert db_runbook.title == sample_runbook_data["title"]

    await runbook_repo.collection.delete_many({})
