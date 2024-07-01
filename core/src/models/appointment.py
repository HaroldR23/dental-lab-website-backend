from typing import NamedTuple


class Appointment(NamedTuple):
    date: str
    time: str
    patient_name: str
    patient_email: str
