from adapters.src.exceptions.repository.product import \
    ProductRepositoryException
from core.src.exceptions.business.product import (
    ProductAlreadyExistsException, ProductBusinessException)
from core.src.models.product import Product
from core.src.repository.product_repository import ProductRepository
from core.src.use_cases.product.create import (CreateProductRequest,
                                               CreateProductResponse)


class CreateProduct:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self, request: CreateProductRequest) -> CreateProductResponse:
        try:
            product = Product(**request._asdict())
            current_product = self.product_repository.get_by_name(request.name)

            if current_product:
                raise ProductAlreadyExistsException(name=request.name)

            product = self.product_repository.create(product=product)

            return CreateProductResponse(
                name=product.name,
            )

        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))
