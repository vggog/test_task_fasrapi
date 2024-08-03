import pymongo
from pymongo.database import Database

from .configs.schemas import DBConfig


def get_db(db_config: DBConfig) -> Database:
    """Function for connecting to mongo and return db"""
    client = pymongo.MongoClient(db_config.connection_string)
    return client[db_config.db_name]
