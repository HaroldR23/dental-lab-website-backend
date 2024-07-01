from unittest.mock import patch

import pytest

from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from adapters.src.repositories.memory.memory_appointment_repository import \
    MemoryAppointmentRepository
from core.src.exceptions.business.appointment import \
    AppointmentBusinessException
from core.src.models.appointment import Appointment
from core.src.use_cases.appointment.get_all import (GetAllAppointments,
                                                    GetAllAppointmentsResponse)


def test_get_all_appointments_return_a_list_of_appointments(
    create_appointments_in_memory,
    get_all_appointments_use_case: GetAllAppointments,
):
    # Arrange
    create_appointments_in_memory

    # Act
    response_use_case: GetAllAppointmentsResponse = get_all_appointments_use_case()
    # Assert
    assert len(response_use_case.appointments) == 3
    for appointment in response_use_case.appointments:
        assert isinstance(appointment, Appointment)


def test_get_all_appointments_return_empty_list_when_no_appointments(
    get_all_appointments_use_case: GetAllAppointments,
):
    # Act
    response_use_case: GetAllAppointmentsResponse = get_all_appointments_use_case()

    # Assert
    assert len(response_use_case.appointments) == 0


def test_get_all_appointments_raise_an_exception_when_something_went_wrong(
    get_all_appointments_use_case: GetAllAppointments,
):
    # Arrange
    error_msg = "Something went wrong trying to get_all the Appointment"

    # Act
    with patch.object(
        MemoryAppointmentRepository,
        "get_all",
        side_effect=AppointmentRepositoryException(method="get_all"),
    ):
        with pytest.raises(AppointmentBusinessException) as exc:
            get_all_appointments_use_case()

    # Assert
    assert str(exc.value) == error_msg
