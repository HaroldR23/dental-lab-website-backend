from typing import List, NamedTuple, Optional


class ProductPrice(NamedTuple):
    value: float
    description: str


class Product(NamedTuple):
    name: str
    prices: List[ProductPrice]
    img_url: str
    id: Optional[str] = None
