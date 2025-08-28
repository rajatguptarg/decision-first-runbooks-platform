"""Unit tests for the security services."""
from unittest.mock import AsyncMock, MagicMock

import pytest
from bson import ObjectId
from fastapi import HTTPException, Request

from backend.models.enums import UserRole
from backend.models.user import User
from backend.services.security import get_current_user, requires_role

pytestmark = pytest.mark.asyncio


@pytest.fixture
def mock_request():
    """Fixture for a mock FastAPI request."""
    request = MagicMock(spec=Request)
    request.cookies = {}
    return request


@pytest.fixture
def mock_db():
    """Fixture for a mock database session."""
    return AsyncMock()


@pytest.fixture
def mock_token_service():
    """Fixture for a mock token service."""
    return MagicMock()


@pytest.fixture
def mock_user_repo():
    """Fixture for a mock user repository."""
    return AsyncMock()


async def test_get_current_user_success(
    mock_request, mock_db, mock_token_service, mock_user_repo
):
    """Test successful retrieval of the current user."""
    user_id = ObjectId()
    mock_request.cookies["access_token"] = "test_token"
    mock_token_service.decode_token.return_value = {"sub": str(user_id)}
    mock_user = User(
        id=user_id,
        username="testuser",
        email="test@example.com",
        password_hash="hashed",
        role=UserRole.VIEWER,
    )
    mock_user_repo.get.return_value = mock_user

    # Patch the UserRepository instantiation
    from backend.services import security

    security.UserRepository = MagicMock(return_value=mock_user_repo)
    security.token_service = mock_token_service

    user = await get_current_user(mock_request, mock_db)
    assert user == mock_user


async def test_get_current_user_no_token(mock_request, mock_db):
    """Test that get_current_user fails with no token."""
    with pytest.raises(HTTPException) as excinfo:
        await get_current_user(mock_request, mock_db)
    assert excinfo.value.status_code == 401


async def test_requires_role_success():
    """Test that requires_role succeeds for a user with the correct role."""
    user = User(
        id=ObjectId(),
        username="testuser",
        email="test@example.com",
        password_hash="hashed",
        role=UserRole.EDITOR,
    )

    async def mock_get_current_user():
        return user

    role_checker = requires_role(UserRole.EDITOR)
    # Manually call the dependency
    result = await role_checker(current_user=await mock_get_current_user())
    assert result == user


async def test_requires_role_failure():
    """Test that requires_role fails for a user with the wrong role."""
    user = User(
        id=ObjectId(),
        username="testuser",
        email="test@example.com",
        password_hash="hashed",
        role=UserRole.VIEWER,
    )

    async def mock_get_current_user():
        return user

    role_checker = requires_role(UserRole.EDITOR)
    with pytest.raises(HTTPException) as excinfo:
        await role_checker(current_user=await mock_get_current_user())
    assert excinfo.value.status_code == 403
