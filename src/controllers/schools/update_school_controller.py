from typing import Optional

from fastapi import HTTPException, status
from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.services.provinces_service import ProvincesService
from src.schemas.inputs.school_schema_input import SchoolSchemaRequest
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class UpdateSchoolController(Controller):
    def handle(self, request: Optional[SchoolSchemaRequest] = None, id: str = None):
        """update school controller"""
        school_repository_database = SchoolRepositoryDatabase()
        province_service = ProvincesService()
        school_service = SchoolService(
            school_repository_database, province_service)

        if not school_service.get_school_by_id(id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="School not found")

        response = school_service.update_school(request, id)
        return response
