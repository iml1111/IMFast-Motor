from fastapi import Request
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


def mongodb_cli(request: Request) -> AsyncIOMotorClient:
    """Get MongoDB Client"""
    return request.app.mongdb_cli


def mongodb(request: Request) -> AsyncIOMotorDatabase:
    """Get MongoDB Database"""
    return request.app.mongodb
