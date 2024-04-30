from typing import Annotated, Optional

from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    StringConstraints,
    field_validator
)


class School(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    name: Annotated[str, StringConstraints(min_length=3)]
    email: EmailStr
    numberOfRooms: int
    province: Annotated[str, StringConstraints(min_length=4)]

    @field_validator('name')
    def name_must_not_be_empty(cls, name: str):
        if not name and len(name) < 3:
            raise ValueError('Name field should contain at least 3 characters')
        return name
