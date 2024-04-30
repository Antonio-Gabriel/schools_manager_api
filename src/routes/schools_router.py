import os
from fastapi import APIRouter, status, File, UploadFile, Query
from src.schemas.inputs.school_schema_input import SchoolSchemaRequest
from src.schemas.responses.schools_schema_response import SchoolsSchemaResponse

from src.controllers.schools.get_schools_controller import GetSchoolsController
from src.controllers.schools.query_school_controller import QuerySchoolController
from src.controllers.schools.update_school_controller import UpdateSchoolController
from src.controllers.schools.delete_school_controller import DeleteSchoolController
from src.controllers.schools.create_school_controller import CreateSchoolController
from src.controllers.schools.schools_bulk_insert_controller import SchoolsBulkInsertController

from src.schemas.responses.client_error_response_model import (
    ClientErrorRespondeModel
)


schools_router = APIRouter(prefix=os.getenv("BASE_URL_PATH"), tags=["Schools"])


@schools_router.post("/schools",
                     status_code=status.HTTP_201_CREATED,
                     response_model=str,
                     responses={
                         400: {
                             "description": "Bad Request - Invalid school data provided",
                             "model": ClientErrorRespondeModel,
                         },
                     }
                     )
def create_school(school: SchoolSchemaRequest) -> str:
    """create new school"""
    create_schools_controller = CreateSchoolController()
    response = create_schools_controller.handle(school)
    return response


@schools_router.get("/schools", status_code=status.HTTP_200_OK, response_model=SchoolsSchemaResponse)
def get_schools(q: str = Query(None, description="Search by name or email")):
    """list all schools registered, or find by name or email"""
    if not q:
        get_schools_controller = GetSchoolsController()
        schools = get_schools_controller.handle()
        return {
            "schools": schools
        }

    query_school_controller = QuerySchoolController()
    schools = query_school_controller.handle(q)
    return {
        "schools": schools
    }


@schools_router.post("/schools/upload/excel",
                     response_model=str,
                     responses={
                         400: {
                             "description": "Bad Request - Invalid school data provided",
                             "model": ClientErrorRespondeModel,
                         },
                     }
                     )
def upload_schools_to_builk_insert(file: UploadFile = File(...)):
    """upload excel file to bulk insert schools"""
    bulk_insert_controller = SchoolsBulkInsertController()
    response = bulk_insert_controller.handle(file)
    return response


@schools_router.put("/schools",
                    status_code=status.HTTP_200_OK,
                    response_model=str,
                    responses={
                        400: {
                            "description": "Bad Request - Invalid school data provided",
                            "model": ClientErrorRespondeModel,
                        },
                        404: {
                            "description": "Not Found - School data not found",
                            "model": ClientErrorRespondeModel,
                        },
                    }
                    )
def update_school(school: SchoolSchemaRequest, id: str) -> str:
    """update a school"""
    update_school_controller = UpdateSchoolController()
    response = update_school_controller.handle(school, id)
    return response


@schools_router.delete("/schools/{school_id}",
                       status_code=status.HTTP_200_OK,
                       response_model=str,
                       responses={
                           400: {
                               "description": "Bad Request - Invalid school data provided",
                               "model": ClientErrorRespondeModel,
                           },
                           404: {
                               "description": "Not Found - School data not found",
                               "model": ClientErrorRespondeModel,
                           },
                       }
                       )
def delete_school(school_id: str) -> str:
    """delete a school"""
    delete_schools_controller = DeleteSchoolController()
    response = delete_schools_controller.handle(school_id)
    return response
