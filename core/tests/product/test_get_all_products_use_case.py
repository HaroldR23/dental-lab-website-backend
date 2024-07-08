from unittest.mock import patch

import pytest

from adapters.src.exceptions import ProductRepositoryException
from adapters.src.repositories import MemoryProductRepository
from core.src.exceptions.business import ProductBusinessException
from core.src.models import Product, ProductPrice
from core.src.use_cases import (CreateProduct, CreateProductRequest,
                                GetAllProducts)


def test_get_all_products_should_return_a_list_of_products(
    product_creation_use_case: CreateProduct, get_all_products_use_case: GetAllProducts
):
    # Arrange
    product1 = Product(
        name="Product 1",
        prices=[
            ProductPrice(description=f"Description {i}", value=i) for i in range(1, 2)
        ],
        img_url="http://test.url",
    )
    product2 = Product(
        name="Product 2",
        prices=[
            ProductPrice(description=f"Description {i}", value=i) for i in range(1, 3)
        ],
        img_url="http://test.url",
    )
    product3 = Product(
        name="Product 3",
        prices=[
            ProductPrice(description=f"Description {i}", value=i) for i in range(1)
        ],
        img_url="http://test.url",
    )
    products = [product1, product2, product3]

    for product in products:
        product_creation_use_case(
            request=CreateProductRequest(
                img_url=product.img_url, name=product.name, prices=product.prices
            )
        )

    # Act
    response_use_case = get_all_products_use_case()
    # Assert
    assert len(response_use_case.products) == 3
    for product in response_use_case.products:
        assert isinstance(product, Product)


def test_get_all_products_should_return_empty_list_when_no_products(
    get_all_products_use_case: GetAllProducts,
):
    # Act
    response_use_case = get_all_products_use_case()

    # Assert
    assert len(response_use_case.products) == 0


def test_get_all_products_should_raise_an_exception_when_something_went_wrong(
    get_all_products_use_case,
):
    # Arrange
    error_msg = "Something went wrong trying to get_all the product."

    # Act
    with patch.object(
        MemoryProductRepository,
        "get_all",
        side_effect=ProductRepositoryException(method="get_all"),
    ):
        with pytest.raises(ProductBusinessException) as exc_info:
            get_all_products_use_case()
            # Assert
            assert str(exc_info.value) == error_msg
