from datetime import timedelta, datetime, UTC
from typing import Annotated

from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from starlette import status

from src.auth.auth import bcrypt_context, oauth2_bearer
from src.core.config import settings
from src.models.user import UserTable


class AuthService:
    def __init__(self, auth_repository):
        self.auth_repository = auth_repository

    async def authenticate_user(self, username: str, password: str) -> UserTable | None:
        user = await self.auth_repository.get_user_by_username(username)
        if not user:
            return None
        if not bcrypt_context.verify(password, user.password):
            return None
        return user

def create_access_token(username: str, user_id: int):
    encode = {'sub': username, "id": user_id}
    expires = datetime.now(UTC) + timedelta(settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    encode.update({'exp': expires})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        if not username or not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")
        return {"id": user_id, "username": username}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user")