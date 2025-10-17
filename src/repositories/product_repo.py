from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.product import ProductTable as ProductSchema
from src.schemas.product import CreateProduct, UpdateProduct


class ProductRepository:
    def __init__(self, session: AsyncSession):
        self.session = session


    async def create_product(self, product_data: CreateProduct):
        db_product = ProductSchema(
            name=product_data.name,
            description=product_data.description,
            calories_per_100g=product_data.calories_per_100g,
            carbs_per_100g=product_data.carbs_per_100g,
            fats_per_100g=product_data.fats_per_100g,
            proteins_per_100g=product_data.proteins_per_100g
        )

        self.session.add(db_product)
        await self.session.commit()
        return db_product


    async def get_product_by_id(self, product_id: int):
        result = await self.session.execute(select(ProductSchema).where(ProductSchema.id == product_id))
        return result.scalar_one_or_none()


    async def update_product(self, product_id: int, product_data: UpdateProduct):
        db_product = await self.get_product_by_id(product_id)
        db_product.name = product_data.name
        db_product.description = product_data.description
        db_product.calories_per_100g = product_data.calories_per_100g
        db_product.carbs_per_100g = product_data.carbs_per_100g
        db_product.fats_per_100g = product_data.fats_per_100g
        db_product.proteins_per_100g = product_data.proteins_per_100g
        await self.session.commit()
        return db_product


    async def delete_product(self, product_id: int):
        db_product = await self.get_product_by_id(product_id)
        await self.session.delete(db_product)
        await self.session.commit()
        return db_product
