import pytest
from sqlalchemy.orm import Session

from adapters.src.exceptions import ProductRepositoryException
from adapters.src.repositories.sql import SQLProductRepository
from core.src.models.product import Product


def test_sql_create_product_adapter_should_return_product_model(
    mock_product_model: Product, mock_session: Session
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_session)
    # Act
    created_product = sql_product_repository.create(product=mock_product_model)
    # Assert
    assert isinstance(created_product, Product)


def test_sql_create_product_adapter_should_raise_an_exception_when_something_went_wrong(
    mock_product_model: Product, mock_bad_commit_session: Session
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_bad_commit_session)
    error_message = "Something went wrong trying to create the Product"
    # Act and Assert
    with pytest.raises(ProductRepositoryException, match=error_message):
        sql_product_repository.create(product=mock_product_model)
