from adapters.src.exceptions.repository.base import RepositoryException


class AppointmentRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Appointment", method=method)
