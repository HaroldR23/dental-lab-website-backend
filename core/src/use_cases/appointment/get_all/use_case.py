from core.src.repository.appointment_repository import AppointmentRepository


class GetAllAppointments:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def __call__(self):
        raise NotImplementedError
