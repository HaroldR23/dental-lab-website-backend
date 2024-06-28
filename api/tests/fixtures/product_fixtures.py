import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from api.src.routers.index import index_router
from api.src.routers.product import product_router
from main import create_app

@pytest.fixture
def client():
    app = create_app()
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_product_payload():
    return {
        "name": "Product 1",
        "img_url": "Product 1 description",
        "price": 10.0
    }
