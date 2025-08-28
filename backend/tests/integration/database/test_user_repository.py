"""Integration tests for the UserRepository."""
import pytest
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.enums import UserRole
from backend.models.user import User
from backend.repositories.user import UserRepository

pytestmark = pytest.mark.integration


@pytest.mark.asyncio
async def test_create_user(test_db: AsyncIOMotorDatabase):
    """Test creating a user."""
    user_repo = UserRepository(test_db)
    await user_repo.collection.delete_many({})

    user_data = User(
        username="testuser",
        email="test@example.com",
        password_hash="hashed_password",
        role=UserRole.EDITOR,
    )

    created_user = await user_repo.create(user_data)
    assert created_user is not None
    assert created_user.id is not None
    assert created_user.username == user_data.username
    assert created_user.email == user_data.email

    db_user = await user_repo.get(created_user.id)
    assert db_user is not None
    assert db_user.username == user_data.username

    await user_repo.collection.delete_many({})
