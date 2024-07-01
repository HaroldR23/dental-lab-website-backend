class BusinessException(Exception):
    pass


class AlreadyExistsNameException(BusinessException):
    def __init__(self, entity_type: str, value: str):
        message = f"The {entity_type} with the name '{value}' already exists."
        super().__init__(message)


class DateAlreadyExistsException(BusinessException):
    def __init__(self, date: str, time: str):
        message = (
            f"The Appointment with the date {date} and time {time} already exists."
        )
        super().__init__(message)
