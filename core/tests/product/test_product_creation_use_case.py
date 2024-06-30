from unittest.mock import patch

import pytest

from adapters.src.exceptions.repository.product import \
    ProductRepositoryException
from adapters.src.repositories.memory.memory_product_repository import \
    MemoryProductRepository
from core.src.exceptions.business.product import ProductAlreadyExistsException, ProductBusinessException
from core.src.use_cases.product.create import CreateProductResponse


def test_create_product_should_return_the_product_as_response(
    product_creation_use_case, product_creation_request
):
    # Act
    product_response = product_creation_use_case(request=product_creation_request)

    # Assert
    assert isinstance(product_response, CreateProductResponse)
    assert product_response.name == "Product 1"


def test_create_product_should_raise_an_exception_when_there_is_a_product_with_same_name(
    product_creation_use_case, product_creation_request
):
    # Arrange
    product_creation_use_case(request=product_creation_request)
    error_msg = (
        f"The Product with the name {product_creation_request.name} already exists."
    )

    # Act
    with pytest.raises(ProductAlreadyExistsException) as exc_info:
        product_creation_use_case(request=product_creation_request)
        # Assert
        assert str(exc_info.value) == error_msg


def test_create_product_should_raise_an_exception_when_something_went_wrong_during_the_creation(
    product_creation_use_case, product_creation_request
):
    # Arrange
    error_msg = "Something went wrong trying to create the product."

    # Act
    with patch.object(
        MemoryProductRepository,
        "create",
        side_effect=ProductRepositoryException(method="create"),
    ):
        with pytest.raises(ProductBusinessException) as exc_info:
            product_creation_use_case(request=product_creation_request)
            # Assert
            assert str(exc_info.value) == error_msg
