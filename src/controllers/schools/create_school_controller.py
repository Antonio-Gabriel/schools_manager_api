from typing import Optional

from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.services.provinces_service import ProvincesService
from src.schemas.inputs.school_schema_input import SchoolSchemaRequest
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class CreateSchoolController(Controller):
    def handle(self, request: Optional[SchoolSchemaRequest] = None):
        """create school controller"""
        school_repository_database = SchoolRepositoryDatabase()
        province_service = ProvincesService()
        school_service = SchoolService(
            school_repository_database, province_service)
        response = school_service.create_school(request)
        return response
