import pytest
from sqlalchemy.orm import Session

from adapters.src.exceptions import ProductRepositoryException
from adapters.src.repositories.sql import SQLProductRepository
from core.src.models.product import Product


def test_get_all_products_should_return_a_list_of_products(
    mock_query_all_session: Session,
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_query_all_session)
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


def test_get_all_products_should_raise_exception_when_error_occurs(
    mock_bad_query_session: Session,
):
    # Arrange
    sql_product_repository = SQLProductRepository(session=mock_bad_query_session)
    error_message = "Something went wrong trying to get_all the Product"
    # Act and Assert
    with pytest.raises(ProductRepositoryException, match=error_message):
        sql_product_repository.get_all()
