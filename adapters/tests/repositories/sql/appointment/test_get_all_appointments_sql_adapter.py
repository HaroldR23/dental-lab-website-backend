import pytest
from sqlalchemy.orm import Session

from adapters.src.exceptions import AppointmentRepositoryException
from adapters.src.repositories.sql import SQLAppointmentRepository
from core.src.models.appointment import Appointment


def test_get_all_appointments_should_return_a_list_of_appointments(
    mock_query_all_session: Session,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(
        session=mock_query_all_session
    )
    # Act
    appointments = sql_appointment_repository.get_all()
    # Assert
    assert all(isinstance(appointment, Appointment) for appointment in appointments)


def test_get_all_appointments_should_return_empty_list_when_no_appointments(
    mock_query_all_return_empty_session: Session,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(
        session=mock_query_all_return_empty_session
    )
    # Act
    appointments = sql_appointment_repository.get_all()
    # Assert
    assert len(appointments) == 0


def test_get_all_appointments_should_raise_an_exception_when_something_went_wrong(
    mock_bad_query_session: Session,
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(
        session=mock_bad_query_session
    )
    error_message = "Something went wrong trying to get_all the Appointment"
    # Act and Assert
    with pytest.raises(AppointmentRepositoryException, match=error_message):
        sql_appointment_repository.get_all()
