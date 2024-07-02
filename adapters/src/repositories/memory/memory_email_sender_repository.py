from core.src.repository.email_sender_repository import EmailSenderRepository


class MemoryEmailSenderRepository(EmailSenderRepository):
    def __init__(self):
        pass

    def send_email_notifications(self, patient_name: str, date: str, time: str) -> None:
        print(f"Sending email to {patient_name} for appointment on {date} at {time}")
