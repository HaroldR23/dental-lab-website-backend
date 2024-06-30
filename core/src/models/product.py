from typing import NamedTuple, Optional


class Product(NamedTuple):
    name: str
    price: float
    img_url: str
    id: Optional[str] = None
