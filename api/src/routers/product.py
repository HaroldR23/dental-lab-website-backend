from fastapi import APIRouter, HTTPException

from api.src.dtos import Product
from core.src.use_cases.product.create.request import CreateProductRequest
from factories.use_cases.product import (create_product_use_case,
                                         get_all_products_use_case)

from .index import index_router

product_router = APIRouter()


@product_router.post("/products", tags=["products"])
async def create_product(product: Product):
    try:
        request = CreateProductRequest(
            name=product.name,
            price=product.price,
            img_url=product.img_url,
        )
        use_case = create_product_use_case()
        response_use_case = use_case(request=request)
        return response_use_case
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


@product_router.get("/products", tags=["products"])
async def get_all_products():
    try:
        use_case = get_all_products_use_case()
        response_use_case = use_case()
        products = response_use_case.products
        return [product._asdict() for product in products] if len(products) > 0 else []
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


index_router.include_router(product_router)
