from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    img_url: str
