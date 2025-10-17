from sqlalchemy import select, insert, update, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth import bcrypt_context
from src.models.user import UserTable
from src.schemas.user import CreateUser, UpdateUser


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: int) -> UserTable | None:
        result = await self.session.execute(select(UserTable).where(UserTable.id == user_id))
        return result.scalar_one_or_none()


    async def get_user_by_email(self, user_email: str) -> UserTable | None:
        result = await self.session.execute(select(UserTable).where(UserTable.email == user_email))
        return result.scalar_one_or_none()

    async def get_user_by_username(self, username: str) -> UserTable | None:
        result = await self.session.execute(select(UserTable).where(UserTable.username == username))
        return result.scalar_one_or_none()



    def create_user(self, user_data: CreateUser):
        db_user = UserTable(
            email=user_data.email,
            username=user_data.username,
            password=bcrypt_context.hash(user_data.password)
        )
        self.session.add(db_user)
        return db_user


    async def update_user(self, user_id: int, new_data: UpdateUser):
        db_user = await self.get_user_by_id(user_id)
        db_user.email = new_data.email
        db_user.username = new_data.username
        db_user.password = new_data.password

        await self.session.commit()
        return db_user


    async def delete_user(self, user_id: int):
        db_user = await self.get_user_by_id(user_id)

        await self.session.delete(db_user)
        await self.session.commit()
        return db_user