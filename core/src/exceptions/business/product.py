from .base import AlreadyExistsNameException, BusinessException


class ProductAlreadyExistsException(AlreadyExistsNameException):
    def __init__(self, name: str):
        super().__init__(entity_type="Product", value=name)


class ProductBusinessException(BusinessException):
    """Product business exception"""
