from core.src.repository.product_repository import ProductRepository


class GetAllProducts:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def __call__(self):
        raise NotImplementedError
