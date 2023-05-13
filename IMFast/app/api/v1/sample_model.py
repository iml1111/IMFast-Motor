from typing import Any
from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorDatabase
from app.depends.common import skip_limit
from app.depends.mongo import mongodb
from model.mongodb.collection import Log, AppConfig, LogSchema
from model.appmodel.log import CreateLog
from app.response import OK, CREATED
from . import api


@api.get(
    '/log',
    summary="Get Sample Log",
    response_model=OK[list[LogSchema]]
)
async def get_sample_log(
    range: tuple = Depends(skip_limit),
    db: AsyncIOMotorDatabase = Depends(mongodb),
):
    skip, limit = range
    logs = Log(db).find(skip=skip, limit=limit)
    logs = [LogSchema(**log) async for log in logs]
    return OK(result=logs)


@api.post(
    '/log',
    summary="Create Sample Log",
    response_model=CREATED[str],
)
async def create_sample_log(
    log: CreateLog,
    db: AsyncIOMotorDatabase = Depends(mongodb),
):
    result = await Log(db).insert_one(log)
    return CREATED(result=str(result.inserted_id))


@api.get(
    '/author',
    summary="Get Author",
    response_model=OK[str])
async def get_author(
    db: AsyncIOMotorDatabase = Depends(mongodb),
):
    author = await AppConfig(db).get_author()
    return OK(result=author['value'])


@api.put(
    '/author',
    summary="Update Author",
    response_model=CREATED[str]
)
async def update_author(
    author: str,
    db: AsyncIOMotorDatabase = Depends(mongodb),
):
    await AppConfig(db).upsert_author(author)
    return CREATED()
