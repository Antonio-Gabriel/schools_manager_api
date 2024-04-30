from typing import List
from bson.objectid import ObjectId

from pymongo import ASCENDING
from src.models.school import School
from src.adapters.mongo_client_adapter import MongoClientAdapter
from src.persistence.school_repository import SchoolRepository


class SchoolRepositoryDatabase(SchoolRepository):
    def __init__(self) -> None:
        self.__mongo_client = MongoClientAdapter.connect()
        self.__db = self.__mongo_client.client.schoolsdb
        self.__collection = self.__db.school

    def save(self, school: School):
        """register a school into db"""
        school_payload = {
            "name": school.name,
            "email": school.email,
            "numberOfRooms": school.numberOfRooms,
            "province": school.province
        }

        self.__collection.insert_one(school_payload)

    def save_bulk(self, schools: List[School]):
        """insert bulk schools into db"""
        school_payloads = [
            {
                "name": school.name,
                "email": school.email,
                "numberOfRooms": school.numberOfRooms,
                "province": school.province
            } for school in schools
        ]

        self.__collection.insert_many(school_payloads)

    def get(self):
        """list schools"""
        schools = self.__collection.find()
        return schools

    def get_emails(self):
        """list all emails"""
        emails = [school['email'] for school in self.__collection.find()]
        return emails

    def get_by_email(self, email: str):
        """list school by email"""
        school = self.__collection.find_one({"email": email})
        return school

    def get_by_id(self, id: str):
        """list school by id"""
        school = self.__collection.find_one({"_id": ObjectId(id)})
        return school

    def find_by_name_or_email(self, query: str):
        """query school by name or email"""
        name_query = {"name": {"$regex": query, "$options": "i"}}
        email_query = {"email": {"$regex": query, "$options": "i"}}
        schools = self.__collection.find(
            {"$or": [name_query, email_query]}
        ).sort("name", ASCENDING)

        return schools

    def update(self, school: School, _id: str):
        """update a school"""
        query = {"_id": ObjectId(_id)}

        school_payload = {
            "name": school.name,
            "email": school.email,
            "numberOfRooms": school.numberOfRooms,
            "province": school.province
        }

        self.__collection.update_many(query, {"$set": school_payload})

    def delete(self, _id: str):
        """delete a school"""
        query = {"_id": ObjectId(_id)}

        self.__collection.delete_one(query)
