"""Base repository with generic CRUD operations."""
from typing import Generic, TypeVar

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import BaseModel

from backend.models.base import BaseDBModel

ModelType = TypeVar("ModelType", bound=BaseDBModel)


class BaseRepository(Generic[ModelType]):
    """Base class for data repositories."""

    def __init__(self, model: type[ModelType], db: AsyncIOMotorDatabase):
        """
        Initializes the repository.

        :param model: The Pydantic model type.
        :param db: The database instance.
        """
        self.model = model
        self.db = db
        self.collection = self.db[model.__name__.lower() + "s"]

    async def get(self, id: str) -> ModelType | None:
        """
        Get a single document by ID.

        :param id: The document ID.
        :return: The document, or None if not found.
        """
        doc = await self.collection.find_one({"_id": ObjectId(id)})
        if doc:
            return self.model(**doc)
        return None

    async def create(self, data: ModelType) -> ModelType:
        """
        Create a new document.

        :param data: The document data.
        :return: The created document.
        """
        doc_dict = data.model_dump(by_alias=True)
        if doc_dict.get("_id") is None:
            doc_dict.pop("_id", None)
        result = await self.collection.insert_one(doc_dict)
        created_doc = await self.collection.find_one({"_id": result.inserted_id})
        return self.model(**created_doc)

    async def update(self, id: str, data: BaseModel) -> ModelType | None:
        """
        Update a document.

        :param id: The document ID.
        :param data: The update data.
        :return: The updated document, or None if not found.
        """
        doc_dict = data.model_dump(exclude_unset=True)
        await self.collection.update_one({"_id": ObjectId(id)}, {"$set": doc_dict})
        updated_doc = await self.collection.find_one({"_id": ObjectId(id)})
        if updated_doc:
            return self.model(**updated_doc)
        return None

    async def delete(self, id: str) -> bool:
        """
        Delete a document.

        :param id: The document ID.
        :return: True if deleted, False otherwise.
        """
        result = await self.collection.delete_one({"_id": ObjectId(id)})
        return result.deleted_count > 0
