"""MongoDB Log AppModel"""
from pydantic import BaseModel


class CreateLog(BaseModel):
    ipv4: str
    url: str
    method: str
    params: dict
    status_code: int

    class Config:
        schema_extra = {"example": {
            "ipv4": "8.8.8.8",
            "url": "http://example.com",
            "method": "GET",
            "params": {},
            "status_code": 200,
        }}