"""MongoDB Log AppModel"""
from pydantic import BaseModel, ConfigDict


class CreateLog(BaseModel):
    ipv4: str
    url: str
    method: str
    body: str
    status_code: int

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "ipv4": "8.8.8.8",
                "url": "/your/api/path",
                "method": "GET",
                "body": "Some body",
                "status_code": 200,
            }
        }
    )