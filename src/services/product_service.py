from src.schemas.product import CreateProduct, Product, UpdateProduct
from src.repositories.product_repo import ProductRepository


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    async def create_product(self, product_data: CreateProduct) -> CreateProduct:
        product = await self.product_repository.create_product(product_data)

        return  CreateProduct.model_validate(product)

    async def get_product_by_id(self, product_id: int) -> Product:
        product = await self.product_repository.get_product_by_id(product_id)
        print(product.__dict__)

        return Product.model_validate(product)

    async def update_product(self, product_id: int, product_data: UpdateProduct) -> UpdateProduct:
        product = await self.product_repository.update_product(product_id, product_data)

        return UpdateProduct.model_validate(product)

    async def delete_product(self, product_id: int) -> Product:
        product = await self.product_repository.delete_product(product_id)

        return Product.model_validate(product)
