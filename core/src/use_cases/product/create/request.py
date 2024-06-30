from typing import NamedTuple


class CreateProductRequest(NamedTuple):
    name: str
    price: float
    img_url: str
