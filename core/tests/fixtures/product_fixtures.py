import pytest

from adapters.src.repositories import MemoryProductRepository
from core.src.use_cases import (CreateProduct, CreateProductRequest,
                                GetAllProducts)


@pytest.fixture
def memory_product_repository() -> MemoryProductRepository:
    memory_product_repository: MemoryProductRepository = MemoryProductRepository()
    return memory_product_repository


@pytest.fixture
def product_creation_use_case(
    memory_product_repository: MemoryProductRepository,
) -> CreateProduct:
    product_creation_use_case: CreateProduct = CreateProduct(
        product_repository=memory_product_repository
    )
    return product_creation_use_case


@pytest.fixture
def get_all_products_use_case(
    memory_product_repository: MemoryProductRepository,
) -> GetAllProducts:
    get_all_products_use_case: GetAllProducts = GetAllProducts(
        product_repository=memory_product_repository
    )
    return get_all_products_use_case


@pytest.fixture
def product_creation_request():
    return CreateProductRequest(
        img_url="https://www.test.com/image.jpg", name="Product 1", prices=[]
    )
