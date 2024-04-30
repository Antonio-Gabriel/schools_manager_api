from typing import Optional

from fastapi import HTTPException, status
from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class QuerySchoolController(Controller):
    def handle(self, query: Optional[str] = None):
        """list all school controller"""
        school_repository_database = SchoolRepositoryDatabase()
        school_service = SchoolService(school_repository_database)

        if query:
            schools_response = school_service.find_by_name_or_email(query)

            if not schools_response:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND, detail="School not found")

        return schools_response
