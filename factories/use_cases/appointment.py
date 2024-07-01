from core.src.use_cases.appointment.create import CreateAppointment
from factories.repositories.appointment import sql_appointment_repository


def create_appointment_use_case() -> CreateAppointment:
    return CreateAppointment(appointment_repository=sql_appointment_repository())
