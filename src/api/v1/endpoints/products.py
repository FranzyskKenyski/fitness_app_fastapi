from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.session import get_db_session_async
from src.schemas.product import CreateProduct, Product, UpdateProduct
from src.repositories.product_repo import ProductRepository
from src.services.product_service import ProductService


router = APIRouter()


@router.post("/product", response_model=CreateProduct)
async def create_product(
        product: CreateProduct,
        db: AsyncSession = Depends(get_db_session_async)
):
    product_repo = ProductRepository(db)
    product_service =ProductService(product_repo)

    try:
        return await product_service.create_product(product)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/product/{product_id}", response_model=Product)
async def get_product(
        product_id: int,
        db: AsyncSession = Depends(get_db_session_async)
):
    product_repo = ProductRepository(db)
    product_service = ProductService(product_repo)

    try:
        return await product_service.get_product_by_id(product_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.put("/product/{product_id}", response_model=UpdateProduct)
async def update_product(
        product_id: int,
        product: UpdateProduct,
        db: AsyncSession = Depends(get_db_session_async)
):
    product_repo = ProductRepository(db)
    product_service = ProductService(product_repo)

    try:
        return await product_service.update_product(product_id, product)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.delete("/product/{product_id}")
async def delete_product(
        product_id: int,
        db: AsyncSession = Depends(get_db_session_async)
):
    product_repo = ProductRepository(db)
    product_service = ProductService(product_repo)

    try:
        return await product_service.delete_product(product_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))