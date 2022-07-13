from datetime import datetime
from typing import Type, Any
from pydantic import BaseModel
from model.mongodb.collection import Model, Schema


class AppConfig(Model):

    class AppConfigSchema(Schema):
        """AppConfig Schema"""
        name: str
        value: Any

        class Config:
            # Document Sample
            schema_extra = {"example": {
                "name": "author",
                "value": {
                    'name': 'IML',
                    'email': 'shin10256@gmail.com'
                },
            }}

    def indexes(self) -> list:
        # TODO Required index
        return []

    async def upsert_author(self, author: str):
        return await self.col.update_one(
            {'name': 'author'},
            {'$set': {
                'value': author,
                'updated_at': datetime.now(),
            }},
            upsert=True
        )

    async def get_author(self):
        return await self.col.find_one(
            {'name': 'author'}
        )