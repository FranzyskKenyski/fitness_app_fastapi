from pydantic import BaseModel

from src.schemas.user import BaseUser


class GetUser(BaseUser):
    pass

class GetToken(BaseModel):
    access_token: str
    token_type: str
