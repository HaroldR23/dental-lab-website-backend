from pydantic import BaseModel


class Appointment(BaseModel):
    date: str
    time: str
    patient_name: str
    patient_email: str
    patient_phone: str
