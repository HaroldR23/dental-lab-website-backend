from typing import List
from abc import ABC, abstractmethod
from core.src.models.product import Product

class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, product_name: int) -> Product:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Product]:
        raise NotImplementedError
