from typing import Any
from pymongo import IndexModel, ASCENDING
from pydantic import ConfigDict
from controller.util import utc_now
from model.mongodb.collection import Model, Schema


class AppConfigSchema(Schema):
    """AppConfig Schema"""
    name: str
    value: Any

    model_config = ConfigDict(
        json_schema_extra={"example": {
            "name": "author",
            "value": {
                'name': 'IML',
                'email': 'shin10256@gmail.com'
            },
        }}
    )


class AppConfig(Model):

    def indexes(self) -> list:
        return [
            IndexModel([('name', ASCENDING)])
        ]

    async def upsert_author(self, author: str):
        return await self.col.update_one(
            {'name': 'author'},
            {'$set': {
                'value': author,
                'updated_at': utc_now(),
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
                'value': utc_now(),
                'updated_at': utc_now(),
            }},
            upsert=True
        )

    async def get_server_startup_date(self):
        return await self.col.find_one(
            {'name': 'server_startup_date'}
        )
