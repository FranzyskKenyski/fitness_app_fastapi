from pydantic import ValidationError
from src.repositories.user_repo import UserRepository
from src.schemas.user import CreateUser, UpdateUser, User
from src.models.user import UserTable


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: CreateUser) -> UserTable:
        CreateUser.model_validate(user_data)

        if await self.user_repository.get_user_by_email(user_data.email):
            raise ValidationError("Email already registered")

        user = self.user_repository.create_user(user_data)
        await self.user_repository.session.commit()
        return user

    async def get_user_by_id(self, user_id: int) -> UserTable:
        user = await self.user_repository.get_user_by_id(user_id)
        return user

    async def update_user(self, user_id, new_data: UpdateUser) -> UpdateUser:
        user = await self.user_repository.update_user(user_id, new_data)
        return UpdateUser.model_validate(user)

    async def delete_user(self, user_id: int) -> User:
        user = await self.user_repository.delete_user(user_id)
        return User.model_validate(user)
