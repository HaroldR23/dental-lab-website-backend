from typing import List
from unittest.mock import patch

from fastapi.testclient import TestClient

from core.src.models.product import Product
from core.src.use_cases.product import CreateProduct, GetAllProducts
from core.src.use_cases.product.get_all.response import GetAllProductsResponse


def test_create_product_successfully(client: TestClient, mock_product_payload: dict):
    mock_response_use_case = {"name": "Product 1"}
    with patch.object(CreateProduct, "__call__", return_value=mock_response_use_case):
        response = client.post("/products", json=mock_product_payload)
        assert response.status_code == 200
        assert response.json() == mock_response_use_case


def test_create_product_should_raise_http_exception_when_something_went_wrong(
    client: TestClient, mock_product_payload: dict
):
    with patch.object(CreateProduct, "__call__", side_effect=Exception("Error")):
        response = client.post("/products", json=mock_product_payload)
        assert response.status_code == 500
        assert response.json() == {"detail": {"message": "Error"}}


def test_get_all_products_should_return_an_empty_list_when_there_is_not_products(
    client: TestClient,
):
    with patch.object(
        GetAllProducts, "__call__", return_value=GetAllProductsResponse(products=[])
    ):
        response = client.get("/products")
        assert response.status_code == 200
        assert response.json() == []


def test_get_all_products_should_return_a_list_of_products(
    client: TestClient, mock_products: List[Product]
):
    with patch.object(
        GetAllProducts,
        "__call__",
        return_value=GetAllProductsResponse(products=mock_products),
    ):
        response = client.get("/products")
        assert response.status_code == 200
        assert response.json() == [
            {
                "name": product.name,
                "img_url": product.img_url,
                "prices": product.prices,
                "id": product.id,
            }
            for product in mock_products
        ]


def test_get_all_products_should_raise_http_exception_when_something_went_wrong(
    client: TestClient,
):
    with patch.object(GetAllProducts, "__call__", side_effect=Exception("Error")):
        response = client.get("/products")
        assert response.status_code == 500
        assert response.json() == {"detail": {"message": "Error"}}
