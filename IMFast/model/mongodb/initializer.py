"""
Model initializer for MongoDB.
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase
from model.mongodb.collection import Log, AppConfig


class ModelInitializer:

    def __init__(self,  db: AsyncIOMotorDatabase):
        self.models = [
            Log,
            AppConfig,
        ]
        self.db = db

    async def init_model(self):
        """Initialize Model"""
        await asyncio.wait([
            self.init_indexes(),
            self.init_author(),
            asyncio.sleep(1)
        ])

    async def init_indexes(self):
        for model in self.models:
            model(db=self.db).create_indexes()

    async def init_author(self):
        author = await AppConfig(db=self.db).get_author()
        if author is None:
            await AppConfig(db=self.db).upsert_author('IML')
