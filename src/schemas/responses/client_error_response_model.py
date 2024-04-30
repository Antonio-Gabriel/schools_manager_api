from pydantic import BaseModel

from src.schemas.responses.exceptions_schema_response import (
    ErrorRespondeModel
)


class ClientErrorRespondeModel(BaseModel):
    detail: ErrorRespondeModel
