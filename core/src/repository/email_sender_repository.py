from abc import ABC, abstractmethod


class EmailSenderRepository(ABC):
    @abstractmethod
    def send_email_notifications(self, patient_name: str, date: str, time: str) -> None:
        raise NotImplementedError
