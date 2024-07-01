import pytest

from core.src.models.appointment import Appointment


@pytest.fixture
def mock_appointment():
    appointment = Appointment(
        date="2021-10-10",
        time="10:00",
        patient_name="John Doe",
        patient_email="john@mail.com",
    )
    return appointment
