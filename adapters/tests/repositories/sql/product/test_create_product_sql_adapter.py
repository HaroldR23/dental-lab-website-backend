import pytest

from adapters.src.exceptions.repository.product import ProductRepositoryException
from adapters.src.repositories.sql.sql_product_adapter import SQLProductRepository
from core.src.models.product import Product
from adapters.src.repositories.sql.config_db.session_manager import Session

def test_sql_create_product_adapter_should_return_product_model(
        mock_product_model: Product,
        mock_session: Session
    ):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_session)
    # Act
    created_product = sql_product_repository.create(product=mock_product_model)
    # Assert
    assert isinstance(created_product, Product)

def test_sql_create_product_adapter_should_raise_an_exception_when_something_went_wrong(
        mock_product_model: Product,
        mock_bad_commit_session: Session
    ):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_bad_commit_session)
    error_message="Something went wrong trying to create the Product"
    # Act and Assert
    with pytest.raises(ProductRepositoryException, match=error_message):
        sql_product_repository.create(product=mock_product_model)
