from typing import List, NamedTuple

from core.src.models.product import Product


class GetAllProductsResponse(NamedTuple):
    products: List[Product]
