from pydantic import BaseModel


class BaseUser(BaseModel):
    email: str
    username: str
    password: str

class CreateUser(BaseUser):

    class Config:
        from_attributes = True

class UpdateUser(BaseUser):

    class Config:
        from_attributes = True


class User(BaseUser):
    id: int

    class Config:
        from_attributes = True


