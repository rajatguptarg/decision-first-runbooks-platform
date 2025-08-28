"""User model."""
from datetime import datetime

from pydantic import BaseModel

from .base import BaseDBModel
from .enums import UserRole


class User(BaseDBModel):
    """User account model."""

    username: str
    email: str
    password_hash: str
    role: UserRole
    last_login: datetime | None = None
    is_active: bool = True


class UserCreate(BaseModel):
    """User creation model."""

    username: str
    email: str
    password: str
    role: UserRole = UserRole.VIEWER


class UserUpdate(BaseModel):
    """User update model."""

    username: str | None = None
    email: str | None = None
    role: UserRole | None = None
    is_active: bool | None = None
