from dataclasses import dataclass


@dataclass
class DBConfig:
    connection_string: str
    db_name: str
