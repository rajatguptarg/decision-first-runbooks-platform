"""JWT token generation and validation service."""
from datetime import UTC, datetime, timedelta

from jose import JWTError, jwt

from backend.config import settings


class TokenService:
    """Service for handling JWT tokens."""

    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
        """
        Create a new access token.

        :param data: The data to encode in the token.
        :param expires_delta: The token's expiration delta.
        :return: The encoded access token.
        """
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now(UTC) + expires_delta
        else:
            expire = datetime.now(UTC) + timedelta(
                minutes=settings.access_token_ttl_min
            )
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, settings.jwt_secret, algorithm="HS256")
        return encoded_jwt

    @staticmethod
    def decode_token(token: str) -> dict | None:
        """
        Decode a JWT token.

        :param token: The token to decode.
        :return: The decoded token payload, or None if invalid.
        """
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=["HS256"],
                options={"verify_exp": True},
            )
            return payload
        except JWTError:
            return None


token_service = TokenService()
