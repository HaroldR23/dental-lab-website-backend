from core.src.use_cases.appointment import (CreateAppointment,
                                            GetAllAppointments)
from factories.repositories.appointment import sql_appointment_repository
from factories.repositories.email import email_repository


def create_appointment_use_case() -> CreateAppointment:
    return CreateAppointment(
        appointment_repository=sql_appointment_repository(),
        email_repository=email_repository(),  # TODO: Use the real email repository when it's done
    )


def get_all_appointments_use_case() -> GetAllAppointments:
    return GetAllAppointments(appointment_repository=sql_appointment_repository())
