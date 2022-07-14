from fastapi import FastAPI
from settings import Settings
from model.mongodb.collection import AppConfig
# from model.mongodb.initializer import ...


async def init_app(app: FastAPI, setting: Settings):
    """"Model init"""
    # update server startup date (if necessary)
    app_config = AppConfig()
    await app_config.upsert_server_startup_date()


