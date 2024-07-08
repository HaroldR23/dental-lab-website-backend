from typing import List, NamedTuple

from core.src.models.product import ProductPrice


class CreateProductRequest(NamedTuple):
    name: str
    prices: List[ProductPrice]
    img_url: str
