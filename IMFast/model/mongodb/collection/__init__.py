import pytz
from typing import Optional
from datetime import datetime
from abc import ABCMeta, abstractmethod
from bson.objectid import ObjectId
from bson.codec_options import CodecOptions
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import Field, BaseModel, ConfigDict, field_serializer
from pymongo.write_concern import WriteConcern
from pymongo.read_concern import ReadConcern
from pymongo.read_preferences import ReadPreference
from controller.util import utc_now


class Schema(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    version: int = Field(default=1, alias="__version__")
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )

    @field_serializer('id')
    def serialize_id(self, id: ObjectId):
        return str(id)


class EmbeddedSchema(BaseModel):

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )


class Model(metaclass=ABCMeta):

    def __init__(
        self, 
        db: AsyncIOMotorDatabase,
        read_concern: Optional[ReadConcern] = None,
        write_concern: Optional[WriteConcern] = None,
        read_preference: Optional[ReadPreference] = None,
    ):
        self.col = db[self.__class__.__name__]
        self.col = self.col.with_options(
            codec_options=CodecOptions(
                tz_aware=True,
                tzinfo=pytz.utc
            ),
            read_concern=read_concern,
            write_concern=write_concern,
            read_preference=read_preference
        )

    @abstractmethod
    def indexes(self) -> list:
        """Collection indexes"""
        return []

    def create_indexes(self):
        """Create index"""
        indexes = self.indexes()
        if indexes:
            self.col.create_indexes(indexes)

    @staticmethod
    def _p(*args) -> dict:
        """projection shortcut method"""
        return {'_id': 0, **{field: 1 for field in args}}


# Collections
from .log import Log, LogSchema
from .app_config import AppConfig, AppConfigSchema


