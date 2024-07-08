from typing import List

from pydantic import BaseModel


class ProductPrice(BaseModel):
    description: str
    value: float


class Product(BaseModel):
    name: str
    prices: List[ProductPrice]
    img_url: str
