from adapters.src.repositories.sql.sql_product_adapter import SQLProductRepository
from adapters.src.repositories.sql.config_db import SessionManager

def sql_product_repository() -> SQLProductRepository:
    return SQLProductRepository(session=SessionManager.get_session())
