from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase


def mongo_client(request: Request) -> AsyncIOMotorClient:
    """Get MongoDB Client"""
    return request.app.mongo_client


def mongo_db(request: Request) -> AgnosticDatabase:
    """Get MongoDB Database"""
    return request.app.mongo_db

