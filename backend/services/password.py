"""Password hashing and verification service."""
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class PasswordService:
    """Service for handling password hashing and verification."""

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """
        Verify a plain password against a hashed password.

        :param plain_password: The plain password.
        :param hashed_password: The hashed password.
        :return: True if the password is correct, False otherwise.
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str) -> str:
        """
        Hash a plain password.

        :param password: The plain password.
        :return: The hashed password.
        """
        return pwd_context.hash(password)


password_service = PasswordService()
