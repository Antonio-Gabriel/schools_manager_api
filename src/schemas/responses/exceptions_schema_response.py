from typing import List
from pydantic import BaseModel, Field


class ValidationErrorResponse(BaseModel):
    msg: List[dict] = Field(..., title="Validation Errors",
                            description="List of validation errors")


class ErrorRespondeModel(BaseModel):
    msg: str = Field(..., title="Common Exception",
                     description="Message indicating the exception provided")
