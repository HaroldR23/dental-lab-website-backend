import uuid

from sqlalchemy import Column, String

from .base import Base


class AppointmentRecord(Base):
    __tablename__ = "appointments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    date = Column(String(255))
    time = Column(String(255))
    patient_name = Column(String(255))
    patient_email = Column(String(255))
    patient_phone = Column(String(255))
