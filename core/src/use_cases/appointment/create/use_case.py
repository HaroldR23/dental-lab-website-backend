from core.src.repository.appointment_repository import AppointmentRepository
from core.src.use_cases.appointment.create.request import \
    CreateAppointmentRequest


class CreateAppointment:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def __call__(self, request: CreateAppointmentRequest):
        raise NotImplementedError
