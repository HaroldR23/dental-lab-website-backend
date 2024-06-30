from abc import ABC, abstractmethod
from typing import List, Optional

from core.src.models.product import Product


class ProductRepository(ABC):
    @abstractmethod
    def create(self, product: Product) -> Product:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, product_name: str) -> Optional[Product]:
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Product]:
        raise NotImplementedError
