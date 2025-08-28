"""Integration tests for the SessionRepository."""
import pytest
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.enums import SessionStatus
from backend.models.session import Session
from backend.repositories.session import SessionRepository

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
async def test_create_session(test_db: AsyncIOMotorDatabase):
    """Test creating a session."""
    session_repo = SessionRepository(test_db)
    await session_repo.collection.delete_many({})

    session_data = Session(
        runbook_id=ObjectId(),
        user_id=ObjectId(),
        status=SessionStatus.ACTIVE,
        current_node_id="node1",
    )
    created_session = await session_repo.create(session_data)

    assert created_session is not None
    assert created_session.id is not None
    assert created_session.runbook_id == session_data.runbook_id

    db_session = await session_repo.get(created_session.id)
    assert db_session is not None
    assert db_session.runbook_id == session_data.runbook_id

    await session_repo.collection.delete_many({})
