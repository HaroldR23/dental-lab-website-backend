from abc import ABC, abstractmethod


class EmailSenderRepository(ABC):
    @abstractmethod
    def send_email_notifications(
        self,
        patient_name: str,
        date: str,
        time: str,
        patient_email: str,
        patient_number: str,
    ) -> None:
        raise NotImplementedError
