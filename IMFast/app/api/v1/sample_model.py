from loguru import logger
from model.mongodb.collection import Log
from model.appmodel.log import CreateLog
from app.response import OK, CREATED
from . import api


@api.get(
    '/sample/log',
    summary="Get Sample Log",
    response_model=OK[list[Log.LogSchema]]
)
async def get_sample_log(skip: int = 0, limit: int = 10):
    logs = await (
        Log().find(skip=skip, limit=limit)
        .to_list(length=limit)
    )
    return logs


@api.post(
    '/sample/log',
    summary="Create Sample Log",
    response_model=CREATED[str],
)
async def create_sample_log(log: CreateLog):
    result = await Log().insert_one(log)
    return CREATED(result=str(result.inserted_id))
