from unittest.mock import patch

import pytest

from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from adapters.src.exceptions.repository.email_sender import \
    EmailSenderRepositoryException
from adapters.src.repositories.memory.memory_appointment_repository import \
    MemoryAppointmentRepository
from adapters.src.repositories.memory.memory_email_sender_repository import \
    MemoryEmailSenderRepository
from core.src.exceptions.business.appointment import \
    AppointmentAlreadyExistsException
from core.src.use_cases.appointment.create import (CreateAppointment,
                                                   CreateAppointmentRequest,
                                                   CreateAppointmentResponse)


def test_create_appointment_successfully(
    appointment_creation_use_case: CreateAppointment,
    appointment_creation_request: CreateAppointmentRequest,
):
    # Act
    appointment_response = appointment_creation_use_case(
        request=appointment_creation_request
    )

    # Assert
    assert isinstance(appointment_response, CreateAppointmentResponse)
    assert appointment_response.patient_name == "patient name 1"


def test_create_appointment_should_raise_an_exception_when_there_is_an_appointment_with_same_date_and_time(
    appointment_creation_use_case: CreateAppointment,
    appointment_creation_request: CreateAppointmentRequest,
):
    # Arrange
    appointment_creation_use_case(request=appointment_creation_request)
    error_msg = f"""
    The Appointment with the date
    {appointment_creation_request.date} and time {appointment_creation_request.time} already exists."""

    # Act
    with pytest.raises(AppointmentAlreadyExistsException) as exc_info:
        appointment_creation_use_case(request=appointment_creation_request)
        # Assert
        assert str(exc_info.value) == error_msg


def test_create_appointment_should_raise_an_exception_when_something_went_wrong_during_the_creation(
    appointment_creation_use_case: CreateAppointment,
    appointment_creation_request: CreateAppointmentRequest,
):
    # Arrange
    error_msg = "Something went wrong trying to create the appointment."

    # Act
    with patch.object(
        MemoryAppointmentRepository,
        "create",
        side_effect=AppointmentRepositoryException(method="create"),
    ):
        with pytest.raises(Exception) as exc_info:
            appointment_creation_use_case(request=appointment_creation_request)
            # Assert
            assert str(exc_info.value) == error_msg


def test_create_appointment_should_raise_an_exception_when_something_went_wrong_trying_to_send_email(
    appointment_creation_use_case: CreateAppointment,
    appointment_creation_request: CreateAppointmentRequest,
):
    # Arrange
    error_msg = "Something went wrong trying to send the Email"

    # Act
    with patch.object(
        MemoryEmailSenderRepository,
        "send_email_notifications",
        side_effect=EmailSenderRepositoryException(method="send"),
    ):
        with pytest.raises(Exception) as exc_info:
            appointment_creation_use_case(request=appointment_creation_request)
            # Assert
            assert str(exc_info.value) == error_msg
