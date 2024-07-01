import pytest


@pytest.fixture
def mock_appointment_payload():
    return {
        "patient_name": "Appointment 1",
        "date": "2022-01-01",
        "time": "10:00",
        "patient_email": "patient@mail.com",
    }
