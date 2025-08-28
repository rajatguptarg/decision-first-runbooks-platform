"""User repository."""
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.user import User
from backend.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    """Repository for User documents."""

    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(User, db)
