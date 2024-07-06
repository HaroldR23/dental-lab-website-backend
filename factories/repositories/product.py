from adapters.src.repositories.sql import SessionManager, SQLProductRepository


def sql_product_repository() -> SQLProductRepository:
    return SQLProductRepository(session=SessionManager.get_session())
