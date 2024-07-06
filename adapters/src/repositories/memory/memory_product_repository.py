from typing import List, Optional

from core.src.models import Product
from core.src.repository import ProductRepository


class MemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products: List[Product] = []

    def create(self, product: Product) -> Product:
        self.products.append(product)
        return product

    def get_by_name(self, product_name: str) -> Optional[Product]:
        product_to_return: Optional[Product] = None
        for product in self.products:
            if product.name == product_name:
                product_to_return = product
            else:
                product_to_return = None
        return product_to_return

    def get_all(self) -> List[Product]:
        return self.products
