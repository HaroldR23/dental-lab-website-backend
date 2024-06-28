from core.src.use_cases.product.create import CreateProduct
from factories.repositories.product import sql_product_repository

def create_product_use_case() -> CreateProduct:
    return CreateProduct(product_repository=sql_product_repository())
