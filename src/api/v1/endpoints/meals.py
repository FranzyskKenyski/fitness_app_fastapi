from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.meal import CreateMeal, Meal, UpdateMeal
from src.database.session import get_db_session_async
from src.repositories.meal_repo import MealRepository
from src.services.meal_service import MealService
from src.auth.auth_service import AuthService


router = APIRouter()

@router.post("/meals",response_model=CreateMeal)
async def create_meal(
        meal: CreateMeal,
        db: AsyncSession = Depends(get_db_session_async)
):
    meal_repo = MealRepository(db)
    meal_service = MealService(meal_repo)

    try:
        return await meal_service.create_meal(meal)
    except Exception as e:
        HTTPException(status_code=400, detail=str(e))

@router.get("/meals/{meal_id}",response_model=Meal)
async def get_meal_by_id(
        meal_id: int,
        db: AsyncSession = Depends(get_db_session_async)
):
    meal_repo = MealRepository(db)
    meal_service = MealService(meal_repo)

    try:
        return await meal_service.get_meal_by_id(meal_id)
    except Exception as e:
        HTTPException(status_code=400, detail=str(e))

@router.put("/meals/{meal_id}",response_model=UpdateMeal)
async def update_meal(
        meal_id: int,
        meal_data: UpdateMeal,
        db: AsyncSession = Depends(get_db_session_async)
):
    meal_repo = MealRepository(db)
    meal_service = MealService(meal_repo)

    try:
        return await meal_service.update_meal(meal_id, meal_data)
    except Exception as e:
        HTTPException(status_code=400, detail=str(e))

@router.delete("/meals/{meal_id}",response_model=Meal)
async def delete_meal(
        meal_id: int,
        db: AsyncSession = Depends(get_db_session_async)
):
    meal_repo = MealRepository(db)
    meal_service = MealService(meal_repo)

    try:
        return await meal_service.delete_meal(meal_id)
    except Exception as e:
        HTTPException(status_code=400, detail=str(e))
