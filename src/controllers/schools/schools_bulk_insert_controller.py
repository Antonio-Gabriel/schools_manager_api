from typing import Optional

from fastapi import UploadFile, HTTPException, status

from src.adapters.file_type_adapter import FileTypeAdapter
from src.adapters.pandas_excel_manager_adapter import PandasExcelManager

from src.controllers.controller import Controller
from src.persistence.school_service import SchoolService
from src.services.provinces_service import ProvincesService
from src.schemas.inputs.school_schema_input import SchoolSchemaRequest
from src.persistence.school_repository_database import SchoolRepositoryDatabase


class SchoolsBulkInsertController(Controller):
    def handle(self, file: Optional[UploadFile] = None):
        """create school controller"""
        if not FileTypeAdapter.is_excel_file(file.file):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="File must be a xls or xlsx")

        schools_data, file_format = PandasExcelManager.read_excel_file(
            file.file)

        if not file_format:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="The data in the file needs to be in a specific format: Name, Email, Number of Rooms, Province")

        if not schools_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Please upload a file with data")

        school_repository_database = SchoolRepositoryDatabase()
        province_service = ProvincesService()
        school_service = SchoolService(
            school_repository_database, province_service)

        schools_schema = []
        for school in schools_data:
            schema = SchoolSchemaRequest(name=school["name"],
                                         email=school["email"],
                                         numberOfRooms=school["numberOfRooms"],
                                         province=school["province"])
            schools_schema.append(schema)

        bulk_insert_response = school_service.insert_bulk_school(
            schools_schema)
        return bulk_insert_response
