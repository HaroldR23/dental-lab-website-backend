import pytest

from core.src.models.appointment import Appointment


@pytest.fixture
def mock_appointment_payload():
    return {
        "patient_name": "Appointment 1",
        "date": "2022-01-01",
        "time": "10:00",
        "patient_email": "patient@mail.com",
        "patient_phone": "123456789",
    }


@pytest.fixture
def mock_appointments():
    return [
        Appointment(
            id=str(i),
            date=f"2022-01-0{i}",
            time=f"10:0{1}",
            patient_name=f"Patient {i}",
            patient_email=f"email@{i}.com",
            patient_phone="123456789",
        )
        for i in range(1, 4)
    ]
