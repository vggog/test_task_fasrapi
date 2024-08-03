from .service import Service
from .repository import Repository
from .db import get_db
from .configs import load_db_configs


def service_builder() -> Service:
    """Function for creating Service class"""
    repository = repository_builder()

    return Service(repository)


def repository_builder() -> Repository:
    """Function for creating Repository class"""
    return Repository(
        get_db(load_db_configs())
    )
