from fastapi import APIRouter, HTTPException

from api.src.dtos.product_dto import Product
from core.src.use_cases.product.create.request import CreateProductRequest
from factories.use_cases.product import create_product_use_case

from .index import index_router

product_router = APIRouter()


@product_router.post("/products")
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


@product_router.get("/products")
async def get_all_products():
    raise NotImplementedError


index_router.include_router(product_router)
