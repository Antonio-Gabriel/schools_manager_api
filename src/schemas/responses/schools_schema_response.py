from typing import List

from pydantic import BaseModel, Field


class SchoolData(BaseModel):
    id: str = Field(None, alias="id")
    name: str
    email: str
    numberOfRooms: int
    province: str


class SchoolsSchemaResponse(BaseModel):
    schools: List[SchoolData]

    class Config:
        from_attributes = True
