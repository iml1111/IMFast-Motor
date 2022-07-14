from datetime import datetime
from typing import Any
from pymongo import IndexModel, ASCENDING
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
        return [
            IndexModel([('name', ASCENDING)])
        ]

    async def upsert_author(self, author: str):
        # TODO: Change Property
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

    async def upsert_server_startup_date(self):
        return await self.col.update_one(
            {'name': 'server_startup_date'},
            {'$set': {
                'value': datetime.now(),
                'updated_at': datetime.now(),
            }},
            upsert=True
        )

    async def get_server_startup_date(self):
        return await self.col.find_one(
            {'name': 'server_startup_date'}
        )
