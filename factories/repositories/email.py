from adapters.src.repositories.memory.memory_email_repository import \
    MemoryEmailRepository
from core.src.repository.email_repository import EmailRepository


def email_repository() -> EmailRepository:
    return MemoryEmailRepository()
