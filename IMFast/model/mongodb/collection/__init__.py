from datetime import datetime
from abc import ABCMeta, abstractmethod
from bson.objectid import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from pydantic import Field, BaseModel
from model.mongodb import mongo_db


class Model(metaclass=ABCMeta):

    def __init__(self, db: AsyncIOMotorDatabase = mongo_db):
        self.col = db[self.__class__.__name__]

    @abstractmethod
    def indexes(self) -> list:
        """Collection indexes"""
        return []

    def create_index(self):
        """Create index"""
        indexes = self.indexes()
        if indexes:
            self.col.create_indexes(indexes)

    def p(self, *args) -> dict:
        """projection shortcut method"""
        return {field: 1 for field in args}


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class Schema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    version: int = Field(default=1, alias="__version__")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        # schema_extra = {"example": {}}


from .log import Log
