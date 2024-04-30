import os

import uvicorn
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from bootstrap import *
from src.controllers.provinces_controller import GetProvincesController
from src.schemas.responses.provinces_schema_response import (
    ProvincesSchemaResponse
)

from pydantic import ValidationError
from src.schemas.responses.exceptions_schema_response import (
    ErrorRespondeModel
)
from src.routes.schools_router import schools_router

app = FastAPI(root_path=os.getenv("BASE_URL_PATH"))

app.title = "Schools API"
app.description = "An application to manage schools informations and provide to anyone"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(ValidationError)
async def validation_exception_handler(_: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(include_url=False)}),
    )


@app.exception_handler(Exception)
async def default_exception_handler(_: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"detail": ErrorRespondeModel(msg=str(exc)).model_dump()}),
    )


@app.get("/", status_code=status.HTTP_200_OK, tags=["🔥 Starting"])
def main():
    """main endpoint to say hello"""
    return {
        "msg": "Welcome to schools api, let's start"
    }


@app.get("/provinces", status_code=status.HTTP_200_OK,
         tags=["Provinces"], response_model=ProvincesSchemaResponse)
def get_provinces():
    """list all provinces available"""
    provinces_controller = GetProvincesController()
    provinces = provinces_controller.handle()
    return {
        "provinces": provinces
    }


app.include_router(schools_router)


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
