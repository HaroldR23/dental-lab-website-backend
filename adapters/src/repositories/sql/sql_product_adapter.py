from adapters.src.exceptions.repository.product import ProductRepositoryException
from core.src.repository.product_repository import ProductRepository
from core.src.models.product import Product

from .config_db.session_manager import Session
from .tables.product import ProductRecord

class SQLProductRepository(ProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, product: Product):
        raise NotImplementedError

    def get_by_name(self, product_name: str):
        raise NotImplementedError
    
    def list(self):
        raise NotImplementedError
    
    