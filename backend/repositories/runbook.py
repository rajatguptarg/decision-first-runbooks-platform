"""Runbook repository."""
from motor.motor_asyncio import AsyncIOMotorDatabase

from backend.models.runbook import Runbook
from backend.repositories.base import BaseRepository


class RunbookRepository(BaseRepository[Runbook]):
    """Repository for Runbook documents."""

    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(Runbook, db)
