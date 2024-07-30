from typing import NamedTuple, Optional


class Appointment(NamedTuple):
    date: str
    time: str
    patient_name: str
    patient_email: str
    patient_phone: str
    id: Optional[str] = None
