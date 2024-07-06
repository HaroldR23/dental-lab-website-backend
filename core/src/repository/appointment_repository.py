from abc import ABC, abstractmethod
from typing import List, Optional

from core.src.models import Appointment


class AppointmentRepository(ABC):
    @abstractmethod
    def create(self, appointment: Appointment) -> Appointment:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> List[Appointment]:
        raise NotImplementedError

    @abstractmethod
    def get_by_date_and_time(self, date: str, time: str) -> Optional[Appointment]:
        raise NotImplementedError
