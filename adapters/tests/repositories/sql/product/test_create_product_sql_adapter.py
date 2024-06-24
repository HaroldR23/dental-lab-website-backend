import pytest

from adapters.src.exceptions.repository.product import ProductRepositoryException
from adapters.src.repositories.sql.sql_product_adapter import SQLProductRepository
from core.src.models.product import Product

def test_sql_create_product_adapter_should_return_product_model(
        sql_product_repository: SQLProductRepository, 
        mock_product_model: Product
    ):
    created_product = sql_product_repository.create(product=mock_product_model)
    assert isinstance(created_product, Product)

def test_sql_create_product_adapter_should_raise_an_exception_when_something_went_wrong(
        sql_product_repository_bad_session: SQLProductRepository, 
        mock_product_model: Product
    ):
    with pytest.raises(ProductRepositoryException):
        sql_product_repository_bad_session.create(product=mock_product_model)
