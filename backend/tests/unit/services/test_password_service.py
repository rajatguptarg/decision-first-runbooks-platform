"""Unit tests for the PasswordService."""
from backend.services.password import password_service


def test_password_hashing():
    """Test that password hashing and verification works correctly."""
    password = "secret_password"
    hashed_password = password_service.get_password_hash(password)

    assert hashed_password is not None
    assert hashed_password != password
    assert password_service.verify_password(password, hashed_password) is True
    assert password_service.verify_password("wrong_password", hashed_password) is False
