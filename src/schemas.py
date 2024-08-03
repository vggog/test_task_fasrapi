from pydantic import BaseModel


class MessageScheme(BaseModel):
    user_id: str
    username: str
    text: str
