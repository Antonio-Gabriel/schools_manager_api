import os

from pymongo.mongo_client import MongoClient


class MongoClientAdapter:
    _instance = None

    def __init__(self) -> None:
        if not MongoClientAdapter._instance:
            self.client = MongoClient(
                os.getenv("MONGO_HOST"),
                username=os.getenv("MONGO_USERNAME"),
                password=os.getenv("MONGO_PASSWORD"))
            from pymongo import ASCENDING
            self.ASCENDING = ASCENDING

            MongoClientAdapter._instance = self

    @classmethod
    def connect(cls):
        """method to get a unique instance of mongodb"""

        if not cls._instance:
            cls._instance = cls()
        return cls._instance
