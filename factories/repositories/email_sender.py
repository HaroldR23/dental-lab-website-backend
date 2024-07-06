from adapters.src.repositories import SMTPEmailSenderRepository
from core.src.repository import EmailSenderRepository


def email_sender_repository() -> EmailSenderRepository:
    return SMTPEmailSenderRepository()
