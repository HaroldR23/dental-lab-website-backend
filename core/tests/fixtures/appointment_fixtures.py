import pytest

from adapters.src.repositories import (MemoryAppointmentRepository,
                                       MemoryEmailSenderRepository)
from core.src.use_cases import (CreateAppointment, CreateAppointmentRequest,
                                GetAllAppointments)


@pytest.fixture
def memory_appointment_repository() -> MemoryAppointmentRepository:
    memory_appointment_repository: MemoryAppointmentRepository = (
        MemoryAppointmentRepository()
    )
    return memory_appointment_repository


@pytest.fixture
def memory_email_sender_repository() -> MemoryEmailSenderRepository:
    memory_email_sender_repository: MemoryEmailSenderRepository = (
        MemoryEmailSenderRepository()
    )
    return memory_email_sender_repository


@pytest.fixture
def appointment_creation_use_case(
    memory_appointment_repository: MemoryAppointmentRepository,
    memory_email_sender_repository: MemoryEmailSenderRepository,
) -> CreateAppointment:
    appointment_creation_use_case: CreateAppointment = CreateAppointment(
        appointment_repository=memory_appointment_repository,
        email_sender_repository=memory_email_sender_repository,
    )
    return appointment_creation_use_case


@pytest.fixture
def appointment_creation_request():
    return CreateAppointmentRequest(
        patient_name="patient name 1",
        date="2021-10-10",
        time="10:00",
        patient_email="patient@email.com",
        patient_phone="123456789",
    )


@pytest.fixture
def create_appointments_in_memory(appointment_creation_use_case):
    for appointment_number in range(1, 4):
        appointment_creation_use_case(
            request=CreateAppointmentRequest(
                patient_name=f"Patient {appointment_number}",
                date=f"2022/01/0{appointment_number}",
                time=f"10:0{appointment_number}",
                patient_email=f"email@{appointment_number}.com",
                patient_phone="123456789",
            )
        )


@pytest.fixture
def get_all_appointments_use_case(
    memory_appointment_repository: MemoryAppointmentRepository,
) -> GetAllAppointments:
    get_all_appointments_use_case = GetAllAppointments(
        appointment_repository=memory_appointment_repository
    )
    return get_all_appointments_use_case
