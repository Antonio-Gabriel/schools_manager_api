from typing import List

from pydantic import BaseModel


class ProvincesData(BaseModel):
    nome: str
    capital: str


class ProvincesSchemaResponse(BaseModel):
    provinces: List[ProvincesData]
