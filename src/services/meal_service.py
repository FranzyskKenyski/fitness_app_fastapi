from src.repositories.meal_repo import MealRepository
from src.schemas.meal import CreateMeal, UpdateMeal
from src.models.meal import MealTable


class MealService:
    def __init__(self, meal_repository: MealRepository):
        self.meal_repository = meal_repository

    async def get_meal_by_id(self, meal_id: int) -> MealTable:
        meal = await self.meal_repository.get_meal_by_id_async(meal_id)
        return meal

    async def create_meal(self, meal_data) -> MealTable:
        CreateMeal.model_validate(meal_data)

        meal = self.meal_repository.add_meal(meal_data)
        await self.meal_repository.commit_meal_async()

        return meal

    async def update_meal(self, meal_id: int, meal_data: UpdateMeal) -> MealTable:
        UpdateMeal.model_validate(meal_data)

        meal = await self.meal_repository.get_meal_by_id_async(meal_id)
        updated_meal = self.meal_repository.update_meal(meal, meal_data)
        await self.meal_repository.commit_meal_async()

        return updated_meal

    async def delete_meal(self, meal_id: int) -> MealTable:
        meal = await self.meal_repository.get_meal_by_id_async(meal_id)
        await self.meal_repository.delete_meal(meal)
        await self.meal_repository.commit_meal_async()

        return meal
