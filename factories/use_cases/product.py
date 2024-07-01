from core.src.use_cases.product import CreateProduct, GetAllProducts
from factories.repositories.product import sql_product_repository


def create_product_use_case() -> CreateProduct:
    return CreateProduct(product_repository=sql_product_repository())


def get_all_products_use_case() -> GetAllProducts:
    return GetAllProducts(product_repository=sql_product_repository())
