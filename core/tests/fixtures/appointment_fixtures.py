import pytest

from adapters.src.repositories.memory.memory_appointment_repository import \
    MemoryAppointmentRepository
from core.src.use_cases.appointment.create import (CreateAppointment,
                                                   CreateAppointmentRequest)


@pytest.fixture
def memory_appointment_repository() -> MemoryAppointmentRepository:
    memory_appointment_repository: MemoryAppointmentRepository = (
        MemoryAppointmentRepository()
    )
    return memory_appointment_repository


@pytest.fixture
def appointment_creation_use_case(
    memory_appointment_repository: MemoryAppointmentRepository,
) -> CreateAppointment:
    appointment_creation_use_case: CreateAppointment = CreateAppointment(
        appointment_repository=memory_appointment_repository
    )
    return appointment_creation_use_case


@pytest.fixture
def appointment_creation_request():
    return CreateAppointmentRequest(
        patient_name="patient name 1",
        date="2021-10-10",
        time="10:00",
        patient_email="patient@email.com",
    )
