from fastapi import FastAPI
from model import mongodb
from model.mongodb.collection import AppConfig
# from model.mongodb.initializer import ...


async def init_app(app: FastAPI) -> None:
    """"Model init"""
    # update server startup date (if necessary)
    app_config = AppConfig(db=app.mongodb)
    await app_config.upsert_server_startup_date()
