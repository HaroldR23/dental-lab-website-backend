from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from core.src.exceptions.business.appointment import (
    AppointmentAlreadyExistsException, AppointmentBusinessException)
from core.src.models.appointment import Appointment
from core.src.repository.appointment_repository import AppointmentRepository
from core.src.use_cases.appointment.create import (CreateAppointmentRequest,
                                                   CreateAppointmentResponse)


class CreateAppointment:
    def __init__(self, appointment_repository: AppointmentRepository):
        self.appointment_repository = appointment_repository

    def __call__(self, request: CreateAppointmentRequest):
        try:
            appointment = Appointment(**request._asdict())
            existing_appointment = self.appointment_repository.get_by_date_and_time(
                date=request.date, time=request.time
            )
            if existing_appointment:
                raise AppointmentAlreadyExistsException(
                    date=request.date, time=request.time
                )

            appointment = self.appointment_repository.create(appointment=appointment)

            return CreateAppointmentResponse(
                patient_name=appointment.patient_name,
            )

        except AppointmentRepositoryException as e:
            raise AppointmentBusinessException(str(e))
