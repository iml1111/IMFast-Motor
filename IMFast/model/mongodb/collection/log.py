from typing import Optional
from pydantic import BaseModel, ConfigDict
from pymongo import IndexModel, ASCENDING
from model.mongodb.collection import Model, Schema


class LogSchema(Schema):
    ipv4: str
    url: str
    method: str
    body: Optional[str] = None
    status_code: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "ipv4": "1.1.1.1",
                "url": "http://example.com",
                "method": "GET",
                "body": "Some body",
                "status_code": 200,
            }
        }
    )


class Log(Model):

    def indexes(self) -> list:
        return [
            IndexModel([('created_at', ASCENDING)])
        ]

    async def insert_one(self, log: BaseModel):
        schemized_log = LogSchema(**log.model_dump())
        return await self.col.insert_one(
            schemized_log.model_dump(exclude={'id'})
        )

    async def insert_one_raw_dict(self, log: dict):
        log = LogSchema(**log)
        return await self.col.insert_one(
            log.model_dump(exclude={'id'})
        )

    def find(self, skip: int, limit: int):
        return (
            self.col.find()
            .sort([("created_at", -1)])
            .skip(skip)
            .limit(limit)
        )


if __name__ == "__main__":
    from bson import ObjectId
    a = LogSchema(
        _id=ObjectId(), ipv4="asd", url="asd",
        method="asd", body="asd", status_code=200)

    print(a)
    print(a.model_dump())
    print(a.model_dump_json())