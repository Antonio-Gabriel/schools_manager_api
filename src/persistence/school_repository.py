from abc import ABC, abstractmethod

from typing import List
from src.models.school import School


class SchoolRepository(ABC):
    """repository for school"""

    @abstractmethod
    def save(self, school: School):
        """register a school into db"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def save_bulk(self, schools: List[School]):
        """insert bulk schools into db"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def get(self):
        """list schools"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def get_emails(self):
        """list all emails"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def get_by_email(self, email: str):
        """list school by email"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def get_by_id(self, id: str):
        """list school by id"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def find_by_name_or_email(self, query: str):
        """query school by name or email"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def update(self, school: School, _id: str):
        """update a school"""
        raise NotImplemented("Method not implemented")

    @abstractmethod
    def delete(self, _id: str):
        """delete a school"""
        raise NotImplemented("Method not implemented")
