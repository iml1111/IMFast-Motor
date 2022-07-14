"""
Model initializer for MongoDB.
"""
import asyncio
from model.mongodb.collection import Log, AppConfig


class ModelInitializer:

    def __init__(self):
        self.models = [
            Log,
            AppConfig,
        ]

    async def init_model(self):
        """Initialize Model"""
        await asyncio.wait([
            self.init_indexes(),
            self.init_author(),
        ])

    async def init_indexes(self):
        for model in self.models:
            model().create_indexes()

    @staticmethod
    async def init_author():
        author = await AppConfig().get_author()
        if author is None:
            await AppConfig().upsert_author('IML')
