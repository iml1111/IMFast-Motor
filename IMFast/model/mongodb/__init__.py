"""
https://www.mongodb.com/developer/languages/python/python-quickstart-fastapi/
"""
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from settings import settings

client = AsyncIOMotorClient(
    settings.mongodb_uri,
    connect=False,
    minPoolSize=1,
    #maxPoolSize=100,
)
db = client[settings.mongodb_db_name]

