"""Session repository."""
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.session import Session
from backend.repositories.base import BaseRepository


class SessionRepository(BaseRepository[Session]):
    """Repository for Session documents."""

    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(Session, db)
