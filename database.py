from pymongo import MongoClient
from settings import *


class Database:
    __instance = None

    @staticmethod
    def get_instance():
        if Database.__instance is None:
            client = MongoClient(MONGODB_DSN)
            Database.__instance = client[MONGODB_DB]
        return Database.__instance
