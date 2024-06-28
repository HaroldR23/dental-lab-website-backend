from typing import List

from core.src.repository.product_repository import ProductRepository
from core.src.models.product import Product

class MemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = []

    def create(self, product: Product) -> Product:
        self.products.append(product)
        return product

    def get_by_name(self, product_name: str) -> List[Product]:
        for product in self.products:
            if product.name == product_name:
                return product
            return None

    def list(self) -> Product:
        return self.products
