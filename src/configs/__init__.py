import os

from .schemas import DBConfig


def load_db_configs() -> DBConfig:
    """Function for loading db_configs"""
    connection_string = os.getenv("DB_CONNECTION_STRING")
    db_name = os.getenv("DB_NAME")

    if connection_string is None:
        raise NameError("Secret DB_CONNECTION_STRING not found.")
    elif db_name is None:
        raise NameError("Secret DB_NAME not found.")

    return DBConfig(
        connection_string=connection_string,
        db_name=db_name,
    )
