class BusinessException(Exception):
    pass


class AlreadyExistsNameException(BusinessException):
    def __init__(self, entity_type: str, value: str):
        message = f"The {entity_type} with the name '{value}' already exists."
        super().__init__(message)
