from typing import List, Optional

from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from core.src.models.appointment import Appointment
from core.src.repository.appointment_repository import AppointmentRepository

from .config_db.session_manager import Session
from .tables.appointment import AppointmentRecord


class SQLAppointmentRepository(AppointmentRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, appointment: Appointment):
        try:
            appointment_to_create = AppointmentRecord(
                date=appointment.date,
                time=appointment.time,
                patient_name=appointment.patient_name,
                patient_email=appointment.patient_email,
            )
            self.session.add(appointment_to_create)
            id = str(appointment_to_create.id)
            self.session.commit()
            return Appointment(
                id=id,
                date=appointment.date,
                time=appointment.time,
                patient_name=appointment.patient_name,
                patient_email=appointment.patient_email,
            )
        except Exception:
            self.session.rollback()
            raise AppointmentRepositoryException(method="create")

    def get_all(self):
        try:
            appointments: List[AppointmentRecord] = self.session.query(
                AppointmentRecord
            ).all()
            return [
                Appointment(
                    id=str(appointment.id),
                    date=str(appointment.date),
                    time=str(appointment.time),
                    patient_name=str(appointment.patient_name),
                    patient_email=str(appointment.patient_email),
                )
                for appointment in appointments
            ]
        except Exception:
            raise AppointmentRepositoryException(method="get_all")

    def get_by_date_and_time(self, date: str, time: str):
        try:
            appointment: Optional[AppointmentRecord] = (
                self.session.query(AppointmentRecord)
                .filter(AppointmentRecord.date == date, AppointmentRecord.time == time)
                .first()
            )
            if appointment:
                return Appointment(
                    id=str(appointment.id),
                    date=str(appointment.date),
                    time=str(appointment.time),
                    patient_name=str(appointment.patient_name),
                    patient_email=str(appointment.patient_email),
                )
            return None
        except Exception:
            raise AppointmentRepositoryException(method="get_by_date_and_time")
