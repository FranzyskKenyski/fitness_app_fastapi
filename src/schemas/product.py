from pydantic import BaseModel


class BaseProduct(BaseModel):
    name: str
    description: str
    calories_per_100g: float
    carbs_per_100g: float
    fats_per_100g: float
    proteins_per_100g: float


class CreateProduct(BaseProduct):

    class Config:
        from_attributes = True


class UpdateProduct(BaseProduct):

    class Config:
        from_attributes = True


class Product(BaseProduct):
    id:int

    class Config:
        from_attributes = True
