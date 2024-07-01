from abc import ABC, abstractmethod
from typing import List

from core.src.models.appointment import Appointment


class AppointmentRepository(ABC):
    @abstractmethod
    def create(self, appointment: Appointment) -> Appointment:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Appointment]:
        raise NotImplementedError
