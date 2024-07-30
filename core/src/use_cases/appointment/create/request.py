from typing import NamedTuple


class CreateAppointmentRequest(NamedTuple):
    date: str
    time: str
    patient_name: str
    patient_email: str
    patient_phone: str
