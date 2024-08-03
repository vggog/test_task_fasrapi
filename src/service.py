from .schemas import MessageScheme
from .repository import Repository


class Service:

    def __init__(self, repository: Repository):
        self.repository = repository

    def get_all_messages(self) -> list[MessageScheme]:
        """Get all messages from db"""
        return self.repository.get_all_messages()

    def add_message(self, message: MessageScheme) -> None:
        """Insert message to db"""
        self.repository.insert_message(message)
