from adapters.src.repositories.sql.config_db import SessionManager
from adapters.src.repositories.sql.sql_appointment_adapter import \
    SQLAppointmentRepository


def sql_appointment_repository() -> SQLAppointmentRepository:
    return SQLAppointmentRepository(session=SessionManager.get_session())
