from pydantic import BaseModel


class BaseMeal(BaseModel):
    meal_name: str
    description: str
    user_id: int
    product_id: int


class Meal(BaseMeal):
    id: int

    class Config:
        from_attribute = True


class CreateMeal(BaseMeal):
    class Config:
        from_attribute = True


class UpdateMeal(BaseMeal):
    class Config:
        from_attribute = True