from core.src.models.appointment import Appointment
from core.src.repository.appointment_repository import AppointmentRepository

from .config_db.session_manager import Session


class SQLAppointmentRepository(AppointmentRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, appointment: Appointment):
        raise NotImplementedError

    def get_all(self):
        raise NotImplementedError

    def get_by_date_and_time(self, date: str, time: str):
        raise NotImplementedError
