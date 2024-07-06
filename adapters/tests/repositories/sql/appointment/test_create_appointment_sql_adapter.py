import pytest
from sqlalchemy.orm import Session

from adapters.src.exceptions import AppointmentRepositoryException
from adapters.src.repositories.sql import SQLAppointmentRepository
from core.src.models.appointment import Appointment


def test_sql_create_appointment_adapter_should_return_appointment(
    mock_appointment: Appointment, mock_session: Session
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(session=mock_session)
    # Act
    created_appointment = sql_appointment_repository.create(
        appointment=mock_appointment
    )
    # Assert
    assert isinstance(created_appointment, Appointment)


def test_sql_create_appointment_adapter_should_raise_an_exception_when_something_went_wrong(
    mock_appointment: Appointment, mock_bad_commit_session: Session
):
    # Arrange
    sql_appointment_repository = SQLAppointmentRepository(
        session=mock_bad_commit_session
    )
    error_message = "Something went wrong trying to create the Appointment"
    # Act and Assert
    with pytest.raises(AppointmentRepositoryException, match=error_message):
        sql_appointment_repository.create(appointment=mock_appointment)
