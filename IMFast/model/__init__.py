from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from settings import Settings
from model import mongodb
from model.mongodb.collection import AppConfig
# from model.mongodb.initializer import ...


async def init_app(
    app: FastAPI,
    setting: Settings,
    mongo_client: AsyncIOMotorClient
) -> None:
    """"Model init"""
    # update server startup date (if necessary)
    mongo_db = mongo_client[setting.mongodb_db_name]
    app_config = AppConfig(db=mongo_db)
    await app_config.upsert_server_startup_date()


