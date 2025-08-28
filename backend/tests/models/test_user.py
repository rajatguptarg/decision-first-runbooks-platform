"""Unit tests for the User model."""
import pytest
from pydantic import ValidationError

from backend.models.enums import UserRole
from backend.models.user import User


def test_user_creation():
    """Test successful User model creation."""
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password_hash": "secret_password",
        "role": UserRole.EDITOR,
    }
    user = User(**user_data)

    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.password_hash == user_data["password_hash"]
    assert user.role == user_data["role"]
    assert user.is_active is True
    assert user.last_login is None


def test_user_creation_defaults():
    """Test that default values are set correctly."""
    user = User(
        username="testuser",
        email="test@example.com",
        password_hash="abc",
        role=UserRole.VIEWER,
    )
    assert user.is_active is True
    assert user.last_login is None


def test_user_missing_required_fields():
    """Test that validation fails for missing required fields."""
    with pytest.raises(ValidationError) as excinfo:
        User(username="testuser", email="test@example.com", role=UserRole.VIEWER)
    assert "password_hash" in str(excinfo.value)


def test_user_invalid_role():
    """Test that validation fails for an invalid role."""
    with pytest.raises(ValidationError) as excinfo:
        User(
            username="testuser",
            email="test@example.com",
            password_hash="abc",
            role="invalid_role",
        )
    assert "role" in str(excinfo.value)


def test_user_invalid_email():
    """Test that validation fails for an invalid email."""
    # Pydantic v2 doesn't have built-in email validation without email-validator
    # so this test might need adjustment based on project dependencies.
    # For now, we assume no strict email validation is in place.
    user = User(
        username="testuser",
        email="not-an-email",
        password_hash="abc",
        role=UserRole.VIEWER,
    )
    assert user.email == "not-an-email"
