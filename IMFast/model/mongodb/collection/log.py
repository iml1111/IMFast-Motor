from model.appmodel.log import CreateLog
from model.mongodb.collection import Model, Schema


class Log(Model):

    class LogSchema(Schema):
        """Log Schema"""
        ipv4: str
        url: str
        method: str
        params: dict
        status_code: int

        class Config:
            schema_extra = {"example": {
                "ipv4": "1.1.1.1",
                "url": "http://example.com",
                "method": "GET",
                "params": {},
                "status_code": 200,
            }}

    def indexes(self) -> list:
        return []

    async def insert_one(self, log: CreateLog):
        schemized_log = self.LogSchema(**log.dict())
        return await self.col.insert_one(schemized_log.dict())

    def find(self, skip: int, limit: int):
        return (
            self.col.find()
            .sort([("created_at", -1)])
            .skip(skip)
            .limit(limit)
        )


if __name__ == '__main__':
    log = Log.CreateLog(
        ipv4="asd",
        url="http://example.com",
        method="GET",
        params={},
        status_code=200,
    )
    from model.mongodb import get_client
    from settings import settings
    import asyncio
    c = get_client(settings.mongodb_uri)
    db = c[settings.mongodb_db_name]
    log_model = Log(db)

    async def main():
        #result = await log_model.insert(log)
        result = log_model.find(0, 10)
        result = await result.to_list(None)
        print(result)

    asyncio.run(main())
