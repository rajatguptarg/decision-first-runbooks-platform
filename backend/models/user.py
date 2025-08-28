"""User model."""
from datetime import datetime

from .base import BaseDBModel
from .enums import UserRole


class User(BaseDBModel):
    """User account model."""

    username: str
    email: str
    hashed_password: str
    role: UserRole
    last_login: datetime | None = None
    is_active: bool = True
