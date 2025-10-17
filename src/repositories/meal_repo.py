from sqlalchemy import select, delete, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas.meal import CreateMeal, UpdateMeal
from src.models.meal import MealTable


class MealRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_meal_by_id_async(self, meal_id: int) -> MealTable:
        meal = await self.session.execute(select(MealTable).where(MealTable.id == meal_id))
        return meal.scalar_one_or_none()

    async def commit_meal_async(self):
        await self.session.commit()

    def add_meal(self, meal_data: CreateMeal) -> MealTable:
        meal = MealTable(
            meal_name = meal_data.meal_name,
            description = meal_data.description,
            user_id = meal_data.user_id,
            product_id = meal_data.product_id
        )
        self.session.add(meal)
        return meal

    def update_meal(self, meal: MealTable, meal_data: UpdateMeal) -> MealTable:
        meal.meal_name = meal_data.meal_name
        meal.description = meal_data.description
        meal.user_id = meal_data.user_id
        return meal

    async def delete_meal(self, meal: MealTable) -> MealTable:
        await self.session.delete(meal)
        return meal