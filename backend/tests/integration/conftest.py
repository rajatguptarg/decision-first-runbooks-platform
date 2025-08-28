"""Pytest configuration for integration tests."""
import asyncio

import pytest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from backend.config import settings


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def db_client(event_loop) -> AsyncIOMotorClient:
    """Session-scoped MongoDB client."""
    client = AsyncIOMotorClient(settings.mongodb_uri)
    yield client
    client.close()


@pytest.fixture
def test_db(db_client: AsyncIOMotorClient) -> AsyncIOMotorDatabase:
    """Fixture to get the database instance for tests."""
    return db_client[settings.db_name]
