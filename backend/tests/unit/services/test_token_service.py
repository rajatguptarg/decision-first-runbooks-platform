"""Unit tests for the TokenService."""
import time
from datetime import timedelta

from backend.services.token import token_service


def test_create_and_decode_token():
    """Test that token creation and decoding works correctly."""
    data = {"sub": "testuser"}
    token = token_service.create_access_token(data)

    assert token is not None

    decoded_payload = token_service.decode_token(token)
    assert decoded_payload is not None
    assert decoded_payload["sub"] == data["sub"]


def test_token_expiration():
    """Test that the token expires correctly."""
    data = {"sub": "testuser"}
    token = token_service.create_access_token(data, expires_delta=timedelta(seconds=1))

    time.sleep(1.5)

    decoded_payload = token_service.decode_token(token)
    assert decoded_payload is None


def test_invalid_token():
    """Test that an invalid token is rejected."""
    decoded_payload = token_service.decode_token("invalid_token")
    assert decoded_payload is None
