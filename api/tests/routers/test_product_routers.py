from unittest.mock import patch

from fastapi.testclient import TestClient

from core.src.use_cases.product.create import CreateProduct


def test_create_product_successfully(client: TestClient, mock_product_payload: dict):
    mock_response_use_case = {"name": "Product 1"}
    with patch.object(CreateProduct, "__call__", return_value=mock_response_use_case):
        response = client.post("/products", json=mock_product_payload)
        print(response.json())
        assert response.status_code == 200
        assert response.json() == mock_response_use_case


def test_create_product_should_raise_http_exception_when_something_went_wrong(
    client: TestClient, mock_product_payload: dict
):
    with patch.object(CreateProduct, "__call__", side_effect=Exception("Error")):
        response = client.post("/products", json=mock_product_payload)
        assert response.status_code == 500
        assert response.json() == {"detail": {"message": "Error"}}
