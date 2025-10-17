from fastapi import APIRouter

from src.api.v1.endpoints import users, products, meals, auth


api_router = APIRouter()

api_router.include_router(users.router, tags=["users"])
api_router.include_router(products.router, tags=["products"])
api_router.include_router(meals.router, tags=["meals"])
api_router.include_router(auth.router, tags=["login"])
