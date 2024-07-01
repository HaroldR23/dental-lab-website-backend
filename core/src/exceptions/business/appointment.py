from .base import BusinessException, DateAlreadyExistsException


class AppointmentAlreadyExistsException(DateAlreadyExistsException):
    def __init__(self, date: str, time: str):
        super().__init__(date=date, time=time)


class AppointmentBusinessException(BusinessException):
    """Product business exception"""
