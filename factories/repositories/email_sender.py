from adapters.src.repositories.email_sender.email_sender_adapter import \
    SMTPEmailSenderRepository
from core.src.repository.email_sender_repository import EmailSenderRepository


def email_sender_repository() -> EmailSenderRepository:
    return SMTPEmailSenderRepository()
