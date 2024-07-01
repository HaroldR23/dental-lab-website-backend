from adapters.src.exceptions.repository.product import \
    ProductRepositoryException
from core.src.exceptions.business.product import ProductBusinessException
from core.src.repository.product_repository import ProductRepository
from core.src.use_cases.product.get_all.response import GetAllProductsResponse


class GetAllProducts:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self):
        try:
            products = self.product_repository.get_all()
            return GetAllProductsResponse(products=products)
        except ProductRepositoryException as e:
            raise ProductBusinessException(str(e))
