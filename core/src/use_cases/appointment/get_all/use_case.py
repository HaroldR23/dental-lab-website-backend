from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from core.src.exceptions.business.appointment import \
    AppointmentBusinessException
from core.src.repository.appointment_repository import AppointmentRepository
from core.src.use_cases.appointment.get_all.response import \
    GetAllAppointmentsResponse


class GetAllAppointments:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def __call__(self):
        try:
            appointments = self.appointment_repository.get_all()
            return GetAllAppointmentsResponse(appointments=appointments)
        except AppointmentRepositoryException as e:
            raise AppointmentBusinessException(str(e))
