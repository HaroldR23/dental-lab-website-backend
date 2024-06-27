import pytest

from adapters.src.repositories.sql.sql_product_adapter import SQLProductRepository
from core.src.models.product import Product

@pytest.fixture
def mock_product_model():
    product = Product(
        name="Test Product",
        price=10.0,
        id="1",
        img_url="http://test.com"
    )
    return product