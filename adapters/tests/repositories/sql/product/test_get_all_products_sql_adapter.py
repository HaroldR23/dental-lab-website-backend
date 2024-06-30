from adapters.src.repositories.sql.config_db.session_manager import Session
from adapters.src.repositories.sql.sql_product_adapter import \
    SQLProductRepository
from core.src.models.product import Product


def test_get_all_products_should_return_a_list_of_products(
    mock_query_all_products_session: Session,
):
    # Arrange
    sql_product_repository = SQLProductRepository(
        session=mock_query_all_products_session
    )
    # Act
    products = sql_product_repository.get_all()
    # Assert
    assert all(isinstance(product, Product) for product in products)


def test_get_all_products_should_return_empty_list_when_no_products(
    mock_query_all_return_empty_session: Session,
):
    # Arrange
    sql_product_repository = SQLProductRepository(
        session=mock_query_all_return_empty_session
    )
    # Act
    products = sql_product_repository.get_all()
    # Assert
    assert len(products) == 0
