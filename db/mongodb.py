from pymongo import MongoClient
import os

MONGODB_CONNECTION_STRING = os.getenv("MONGODB_CONNECTION_STRING")


class MongoDb:
    @staticmethod
    def get_connection():
        return MongoClient(MONGODB_CONNECTION_STRING)
