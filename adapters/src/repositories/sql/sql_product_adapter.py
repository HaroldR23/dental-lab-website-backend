from adapters.src.exceptions.repository.product import ProductRepositoryException
from core.src.repository.product_repository import ProductRepository
from core.src.models.product import Product

from .config_db.session_manager import Session
from .tables.product import ProductRecord

class SQLProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, product: Product):
        try:
            product_to_create = ProductRecord(
                name=product.name,
                price=product.price,
                img_url=product.img_url
            )
            with self.session as session:
                self.session.add(product_to_create)
                id = product_to_create.id
                self.session.commit()
                return Product(
                    **{
                        "id": id,
                        **product._asdict()
                    }
                )
        except Exception as e:
            self.session.rollback()
            raise ProductRepositoryException(method="create")

    def get_by_name(self, product_name: str):
        raise NotImplementedError
    
    def list(self):
        raise NotImplementedError
    
    