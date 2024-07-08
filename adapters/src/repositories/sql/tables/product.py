import uuid

from sqlalchemy import JSON, Column, String

from .base import Base


class ProductRecord(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255))
    prices = Column(JSON)
    img_url = Column(String(255))
