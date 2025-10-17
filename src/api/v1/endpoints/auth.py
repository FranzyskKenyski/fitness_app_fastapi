from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from src.auth.auth_service import AuthService
from src.repositories.user_repo import UserRepository
from src.auth.schemas import GetToken
from src.database.session import get_db_session_async

router = APIRouter()

@router.post("/login", response_model=GetToken)
async def login(
        login_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        db: AsyncSession = Depends(get_db_session_async)
):
    auth_repo = UserRepository(db)
    auth_service = AuthService(auth_repo)

    user = await auth_service.authenticate_user(login_data.username, login_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    token = auth_service.create_access_token(user.username, user.id)

    return {"access_token": token, "token_type": "bearer"}
