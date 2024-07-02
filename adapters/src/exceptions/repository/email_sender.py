from adapters.src.exceptions.repository.base import RepositoryException


class EmailSenderRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Email", method=method)
