import pytest
from fastapi.testclient import TestClient

from core.src.models.product import Product
from main import create_app


@pytest.fixture
def client():
    app = create_app()
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_product_payload():
    return {"name": "Product 1", "img_url": "Product 1 description", "prices": []}


@pytest.fixture
def mock_products():
    return [
        Product(
            name=f"Product {i}",
            img_url=f"http://url_img_{i}.png",
            prices=[],
            id=str(i),
        )
        for i in range(1, 4)
    ]
