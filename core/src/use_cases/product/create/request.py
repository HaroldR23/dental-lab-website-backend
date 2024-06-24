from typing import NamedTuple

class CreateProductRequest(NamedTuple):
    name: str
    price: float
    image_url: str
