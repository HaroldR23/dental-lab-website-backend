from adapters.src.repositories.memory.memory_email_sender_repository import \
    MemoryEmailSenderRepository
from core.src.repository.email_sender_repository import EmailSenderRepository


def email_sender_repository() -> EmailSenderRepository:
    return MemoryEmailSenderRepository()
