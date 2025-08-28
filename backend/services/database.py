"""Database connection and utilities."""
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from backend.config import settings


class Database:
    """Database connection manager."""

    client: AsyncIOMotorClient | None = None
    db: AsyncIOMotorDatabase | None = None

    async def connect(self):
        """Connect to the MongoDB database."""
        self.client = AsyncIOMotorClient(settings.mongodb_uri)
        self.db = self.client[settings.db_name]
        print(f"Connected to MongoDB at {settings.mongodb_uri}")

    async def disconnect(self):
        """Disconnect from the MongoDB database."""
        if self.client:
            self.client.close()
            print("Disconnected from MongoDB")


db = Database()


async def get_db() -> AsyncIOMotorDatabase:
    """FastAPI dependency to get the database instance."""
    if db.db is None:
        raise Exception("Database is not connected")
    return db.db
