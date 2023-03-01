"""
https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/
"""
from motor.motor_asyncio import AsyncIOMotorClient
from settings import settings


def get_client(
        uri: str = settings.mongodb_uri
) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        uri,
        connect=False,
        minPoolSize=1,
        maxPoolSize=100,
    )


mongo_client: AsyncIOMotorClient = get_client(settings.mongodb_uri)
