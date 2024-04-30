from typing import Optional

from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class GetSchoolsController(Controller):
    def handle(self, request: Optional[any] = None):
        """list all school controller"""
        school_repository_database = SchoolRepositoryDatabase()
        school_service = SchoolService(school_repository_database)
        schools_response = school_service.get_schools()
        return schools_response
