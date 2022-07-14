from typing import Any
from fastapi import Depends
from loguru import logger
from app.depends.common import skip_limit
from model.mongodb.collection import Log, AppConfig
from model.appmodel.log import CreateLog
from app.response import OK, CREATED
from . import api


@api.get(
    '/log',
    summary="Get Sample Log",
    response_model=OK[list[Log.LogSchema]]
)
async def get_sample_log(range: tuple = Depends(skip_limit)):
    skip, limit = range
    logs = await (
        Log().find(skip=skip, limit=limit)
        .to_list(length=limit)
    )
    logs = [Log.LogSchema(**log) for log in logs]
    return OK(result=logs)


@api.post(
    '/log',
    summary="Create Sample Log",
    response_model=CREATED[str],
)
async def create_sample_log(log: CreateLog):
    result = await Log().insert_one(log)
    return CREATED(result=str(result.inserted_id))


@api.get(
    '/author',
    summary="Get Author",
    response_model=OK[Any])
async def get_author():
    author = await AppConfig().get_author()
    return OK(result=author['value'])


@api.put(
    '/author',
    summary="Update Author",
    response_model=CREATED[Any]
)
async def update_author(author: str):
    await AppConfig().upsert_author(author)
    return CREATED()
