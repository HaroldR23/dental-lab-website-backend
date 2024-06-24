from adapters.src.exceptions.repository.product import ProductRepositoryException

from core.src.use_cases.product.create import CreateProductRequest, CreateProductResponse
from core.src.exceptions.business.product import ProductAlreadyExistsException, ProductBusinessException
from core.src.repository.product_repository import ProductRepository

class CreateProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self, request: CreateProductRequest) -> CreateProductResponse:
        raise NotImplementedError
