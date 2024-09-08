from typing import Optional

from adapters.src.exceptions import ProductRepositoryException
from core.src.models import Product, ProductPrice
from core.src.repository import ProductRepository

from .config_db.session_manager import Session
from .tables.product import ProductRecord


class SQLProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, product: Product):
        try:
            product_to_create = ProductRecord(
                name=product.name,
                prices=[price._asdict() for price in product.prices],
                img_url=product.img_url,
            )
            self.session.add(product_to_create)
            id = str(product_to_create.id)
            self.session.commit()
            return Product(
                id=id, name=product.name, prices=product.prices, img_url=product.img_url
            )
        except Exception:
            self.session.rollback()
            raise ProductRepositoryException(method="create")

    def get_by_name(self, product_name: str):
        try:
            product: Optional[ProductRecord] = (
                self.session.query(ProductRecord)
                .filter(ProductRecord.name == product_name)
                .first()
            )

            if product:
                return Product(
                    id=str(product.id),
                    name=str(product.name),
                    prices=[
                        ProductPrice(
                            description=price["description"], value=price["value"]
                        )
                        for price in list(product.prices)
                    ],
                    img_url=str(product.img_url),
                )
            return None
        except Exception:
            raise ProductRepositoryException(method="get_by_name")

    def get_all(self):
        try:
            products = self.session.query(ProductRecord).all()
            return [
                Product(
                    id=str(product.id),
                    name=str(product.name),
                    prices=[
                        ProductPrice(
                            description=price["description"], value=price["value"]
                        )
                        for price in list(product.prices)
                    ],
                    img_url=str(product.img_url),
                )
                for product in products
            ]
        except Exception:
            raise ProductRepositoryException(method="get_all")
