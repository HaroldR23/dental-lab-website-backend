from core.src.use_cases.appointment import (CreateAppointment,
                                            GetAllAppointments)
from factories.repositories.appointment import sql_appointment_repository


def create_appointment_use_case() -> CreateAppointment:
    return CreateAppointment(appointment_repository=sql_appointment_repository())


def get_all_appointments_use_case() -> GetAllAppointments:
    return GetAllAppointments(appointment_repository=sql_appointment_repository())
