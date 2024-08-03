from pymongo.database import Database
from pymongo.collection import Collection

from .schemas import MessageScheme


class Repository:

    def __init__(self, db: Database):
        self.collection: Collection = db["messages"]

    def get_all_messages(self):
        """Method for getting all messages from collection"""
        return self.collection.find()

    def insert_message(self, message: MessageScheme) -> None:
        """Method for insert message to collection"""
        self.collection.insert_one(message.__dict__)
