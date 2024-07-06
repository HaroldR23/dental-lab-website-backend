import pytest
from sqlalchemy.orm import Session

from adapters.src.exceptions import ProductRepositoryException
from adapters.src.repositories.sql import SQLProductRepository
from core.src.models.product import Product


def test_get_by_name_adapter_should_return_none_when_does_not_find_any_product(
    mock_none_response: Session,
    mock_product_model: Product,
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_none_response)
    product_name = mock_product_model.name
    # Act
    product = sql_product_repository.get_by_name(product_name=product_name)
    # Assert
    assert product is None


def test_get_by_name_adapter_should_return_product_when_find_product(
    mock_session: Session,
    mock_product_model: Product,
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_session)
    product_name = mock_product_model.name
    # Act
    product = sql_product_repository.get_by_name(product_name=product_name)
    # Assert
    assert isinstance(product, Product)


def test_get_by_name_adapter_should_raise_an_exception_when_something_went_wrong(
    mock_bad_query_session: Session,
    mock_product_model: Product,
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_bad_query_session)
    product_name = mock_product_model.name
    error_message = "Something went wrong trying to get_by_name the Product"
    # Act and Assert
    with pytest.raises(ProductRepositoryException, match=error_message):
        sql_product_repository.get_by_name(product_name=product_name)
