import pytest

from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from adapters.src.repositories.sql.config_db.session_manager import Session
from adapters.src.repositories.sql.sql_appointment_adapter import \
    SQLAppointmentRepository
from core.src.models.appointment import Appointment


def test_get_by_date_and_time_adapter_should_return_appointment_when_find_appointment(
    mock_session: Session,
    mock_appointment: Appointment,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(session=mock_session)
    date = mock_appointment.date
    time = mock_appointment.time
    # Act
    appointment = sql_appointment_repository.get_by_date_and_time(date=date, time=time)
    # Assert
    assert isinstance(appointment, Appointment)


def test_get_by_date_and_time_adapter_should_return_none_when_does_not_find_any_appointment(
    mock_none_response: Session,
    mock_appointment: Appointment,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(session=mock_none_response)
    date = mock_appointment.date
    time = mock_appointment.time
    # Act
    appointment = sql_appointment_repository.get_by_date_and_time(date=date, time=time)
    # Assert
    assert appointment is None


def test_get_by_date_and_time_adapter_should_raise_an_exception_when_something_went_wrong(
    mock_bad_query_session: Session,
    mock_appointment: Appointment,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(
        session=mock_bad_query_session
    )
    date = mock_appointment.date
    time = mock_appointment.time
    error_message = (
        "Something went wrong trying to get_by_date_and_time the Appointment"
    )
    # Act and Assert
    with pytest.raises(AppointmentRepositoryException, match=error_message):
        sql_appointment_repository.get_by_date_and_time(date=date, time=time)
