from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.auth_service import get_current_user
from src.database.session import get_db_session_async
from src.services.user_service import UserService
from src.repositories.user_repo import UserRepository
from src.schemas.user import CreateUser, UpdateUser, User

router = APIRouter()
user_dependency = Annotated[dict, Depends(get_current_user)]

@router.post("/users", response_model=CreateUser)
async def create_user(
        user: CreateUser,
        db: AsyncSession = Depends(get_db_session_async)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)

    try:
        return await user_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/users", response_model=User)
async def get_users(
        user: user_dependency,
        db: AsyncSession = Depends(get_db_session_async)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_id = user.get("id")

    try:
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")

        return await user_service.get_user_by_id(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.put("/users", response_model=UpdateUser)
async def update_user(
        user: user_dependency,
        update_info: UpdateUser,
        db: AsyncSession = Depends(get_db_session_async)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_id = user.get("id")

    try:
        return await user_service.update_user(user_id, update_info)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/users")
async def delete_user(
        user: user_dependency,
        db: AsyncSession = Depends(get_db_session_async)
):
    user_repo = UserRepository(db)
    user_service = UserService(user_repo)
    user_id = user.get("id")

    try:
        return await user_service.delete_user(user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))