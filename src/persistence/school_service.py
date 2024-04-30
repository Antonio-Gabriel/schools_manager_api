from typing import List
from src.models.school import School
from src.persistence.dto.create_school_request_dto import (
    CreateSchoolRequestDTO
)
from src.persistence.dto.update_school_request_dto import (
    UpdateSchoolRequestDTO
)
from src.persistence.school_repository import SchoolRepository
from src.persistence.exceptions.school_not_found import SchoolNotFound
from src.persistence.exceptions.email_already_exists import EmailAlreadyExists
from src.persistence.exceptions.province_not_available import (
    ProvinceNotAvailable
)

from src.services.interfaces.provinces_service_interface import (
    ProvincesServiceInterface
)


class SchoolService:
    def __init__(self, school_repository: SchoolRepository, province_service: ProvincesServiceInterface = None) -> None:
        self.__school_service = school_repository
        self.__provinces_service = province_service

    def create_school(self, school_request_dto: CreateSchoolRequestDTO) -> str:
        """create a new school"""

        school_model = School(
            name=school_request_dto.name,
            email=school_request_dto.email,
            numberOfRooms=school_request_dto.numberOfRooms,
            province=school_request_dto.province
        )

        if self.__school_service.get_by_email(school_model.email):
            raise EmailAlreadyExists(
                "Email already exists associated to an institution")

        if not self.__provinces_service.find_province(school_model.province):
            raise ProvinceNotAvailable("Province choosed not available")

        self.__school_service.save(school_model)

        return "School created successfully"

    def insert_bulk_school(self, school_request_dto: List[CreateSchoolRequestDTO]) -> str:
        """insert bulk school"""
        existing_emails = set(self.__school_service.get_emails())

        school_models = [
            School(
                name=school.name,
                email=school.email,
                numberOfRooms=school.numberOfRooms,
                province=school.province
            ) for school in school_request_dto
        ]

        for school_model in school_models:
            if not school_model.email in existing_emails and (
                self.__provinces_service.find_province(school_model.province)
            ):
                existing_emails.add(school_model.email)
                self.__school_service.save(school_model)

        return "Schools created successfully"

    def get_schools(self):
        """list all schools"""
        schools = []
        for school in self.__school_service.get():
            school['_id'] = str(school['_id'])
            school_model = School(**school)
            schools.append(school_model)

        return schools

    def get_school_by_id(self, id: str):
        """get school by id"""
        return self.__school_service.get_by_id(id)

    def find_by_name_or_email(self, query: str):
        """query school by name or email"""
        schools = []
        for school in self.__school_service.find_by_name_or_email(query):
            school['_id'] = str(school['_id'])
            school_model = School(**school)
            schools.append(school_model)

        return schools

    def update_school(self, school_request_dto: UpdateSchoolRequestDTO, id: str) -> str:
        """update school"""

        school_model = School(
            name=school_request_dto.name,
            email=school_request_dto.email,
            numberOfRooms=school_request_dto.numberOfRooms,
            province=school_request_dto.province
        )

        current_school = self.__school_service.get_by_id(id)

        if current_school["email"] != school_model.email:
            if self.__school_service.get_by_email(school_model.email):
                raise EmailAlreadyExists(
                    "Email already exists associated to an institution")

        if not self.__provinces_service.find_province(school_model.province):
            raise ProvinceNotAvailable("Province choosed not available")

        self.__school_service.update(school_model, id)
        return "School updated successfully"

    def delete_school(self, id: str):
        """delete school"""
        school_found = self.__school_service.get_by_id(id)
        if not school_found:
            raise SchoolNotFound("School not found")

        self.__school_service.delete(id)
        return "School deleted successfully"
