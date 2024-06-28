from sqlalchemy import Column, Integer, String, Float
import uuid

from .base import Base


class ProductRecord(Base):
    __tablename__ = 'products'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255))
    price = Column(Float)
    img_url = Column(String(255))
