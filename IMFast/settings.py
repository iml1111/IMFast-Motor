import os
from pydantic import BaseSettings, Field
from fastapi import FastAPI

__AUTHOR__ = "IML"
__VERSION__ = "0.1.1"

APP_NAME = "IMFast"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    # Description settings
    app_name: str = Field(APP_NAME, env='APP_NAME')
    description: str = "Welcome to IMFast."
    term_of_service: str = "https://github.com/iml1111"
    contact_name: str = __AUTHOR__
    contact_url: str = "https://github.com/iml1111"
    contact_email: str = "shin10256@gmail.com"
    # Documentation url
    docs_url: str = "/docs"
    # JWT settings
    secret_key: str = "super-secret"
    jwt_algorithm: str = "HS256"
    jwt_access_expires: int = 3600 * 24 * 7
    jwt_refresh_expires: int = 3600 * 24 * 30
    # Slow API settings
    slow_api_time: float = 0.5
    # Mongodb settings
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db_name: str = "Imfast"
    mongodb_api_log: bool = True

    class Config:
        env_prefix = f"{APP_NAME.upper()}_"
        # default: development env
        env_file = BASE_DIR + '/dev.env'
        env_file_encoding = 'utf-8'

    def init_app(self, app: FastAPI):
        ...


class TestSettings(Settings):
    """Test settings"""
    slow_api_time: float = 1.0


settings = Settings()
