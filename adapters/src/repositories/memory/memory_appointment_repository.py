from typing import List, Optional

from core.src.models.appointment import Appointment
from core.src.repository.appointment_repository import AppointmentRepository


class MemoryAppointmentRepository(AppointmentRepository):
    def __init__(self):
        self.appointments: List[Appointment] = []

    def create(self, appointment: Appointment) -> Appointment:
        self.appointments.append(appointment)
        return appointment

    def get_by_date_and_time(self, date: str, time: str) -> Optional[Appointment]:
        appointment_to_return: Optional[Appointment] = None
        for appointment in self.appointments:
            if appointment.date == date and appointment.time == time:
                appointment_to_return = appointment
            else:
                appointment_to_return = None
        return appointment_to_return

    def get_all(self) -> List[Appointment]:
        raise NotImplementedError
