from fastapi import APIRouter, HTTPException
from .index import index_router
from api.src.dtos.product_dto import Product
from factories.use_cases.product import create_product_use_case

product_router = APIRouter()

@product_router.post("/products")
async def create_product(product: Product):
    try:
        use_case = create_product_use_case()
        response_use_case = use_case(request=product)
        return response_use_case
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})

index_router.include_router(product_router)
