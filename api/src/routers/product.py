from fastapi import APIRouter, HTTPException
from .index import index_router
from api.src.dtos.product_dto import Product

product_router = APIRouter()

@product_router.post("/products")
async def create_product(product: Product):
    raise NotImplementedError

index_router.include_router(product_router)
