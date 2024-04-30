from pydantic import BaseModel, Field


class SchoolSchemaRequest(BaseModel):
    name: str = Field(..., title="Name", description="The name of the school")
    email: str = Field(..., title="Email",
                       description="The email of the school")
    numberOfRooms: int = Field(..., title="Number Of Rooms",
                               description="The number of rooms of the school")
    province: str = Field(..., title="Province",
                          description="The province of the school")

    class Config:
        from_attributes = True
