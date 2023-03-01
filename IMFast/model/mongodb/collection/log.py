from typing import Type, Optional
from pydantic import BaseModel
from pymongo import IndexModel, ASCENDING
from model.mongodb.collection import Model, Schema


class LogSchema(Schema):
        """Log Schema"""
        ipv4: str
        url: str
        method: str
        body: Optional[str] = None
        status_code: int

        class Config:
            # Document Sample
            schema_extra = {"example": {
                "ipv4": "1.1.1.1",
                "url": "http://example.com",
                "method": "GET",
                "body": "Some body",
                "status_code": 200,
            }}


class Log(Model):

    SCHEMA = LogSchema

    def indexes(self) -> list:
        return [
            IndexModel([('created_at', ASCENDING)])
        ]

    async def insert_one(self, log: Type[BaseModel]):
        schemized_log = self.schemaize(log.dict())
        return await self.col.insert_one(
            schemized_log.dict(exclude={'id'})
        )

    async def insert_one_raw_dict(self, log: dict):
        log = self.schemaize(log)
        return await self.col.insert_one(
            log.dict(exclude={'id'})
        )

    def find(self, skip: int, limit: int):
        return (
            self.col.find()
            .sort([("created_at", -1)])
            .skip(skip)
            .limit(limit)
        )
