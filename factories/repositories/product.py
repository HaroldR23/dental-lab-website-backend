from adapters.src.repositories.sql.config_db import SessionManager
from adapters.src.repositories.sql.sql_product_adapter import \
    SQLProductRepository


def sql_product_repository() -> SQLProductRepository:
    return SQLProductRepository(session=SessionManager.get_session())
