from adapters.src.repositories.sql import (SessionManager,
                                           SQLAppointmentRepository)


def sql_appointment_repository() -> SQLAppointmentRepository:
    return SQLAppointmentRepository(session=SessionManager.get_session())
