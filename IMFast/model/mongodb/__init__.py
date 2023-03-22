"""
https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
https://www.mongodb.com/developer/languages/python/farm-stack-fastapi-react-mongodb/
"""
from motor.motor_asyncio import AsyncIOMotorClient


def get_client(uri: str) -> AsyncIOMotorClient:
    return AsyncIOMotorClient(
        uri,
        connect=False,
        minPoolSize=1,
        maxPoolSize=100,
    )
