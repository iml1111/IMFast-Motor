"""
https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/
"""
from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings


mongo_client = AsyncIOMotorClient(
    settings.mongodb_uri,
    connect=False,
    minPoolSize=1,
    maxPoolSize=100,
)
mongo_db = mongo_client[settings.mongodb_db_name]


def get_client(uri: str) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        uri, connect=False,
        minPoolSize=1, maxPoolSize=100,
    )



