from typing import Optional

from fastapi import HTTPException, status
from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class DeleteSchoolController(Controller):
    def handle(self, request: Optional[str] = None):
        """delete school controller"""
        school_repository_database = SchoolRepositoryDatabase()
        school_service = SchoolService(school_repository_database)

        try:
            delete_response = school_service.delete_school(request)
            return delete_response
        except Exception as ex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=str(ex))
