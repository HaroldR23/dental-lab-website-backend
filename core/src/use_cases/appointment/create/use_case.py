from adapters.src.exceptions.repository.appointment import \
    AppointmentRepositoryException
from adapters.src.exceptions.repository.email_sender import \
    EmailSenderRepositoryException
from core.src.exceptions.business.appointment import (
    AppointmentAlreadyExistsException, AppointmentBusinessException)
from core.src.models.appointment import Appointment
from core.src.repository.appointment_repository import AppointmentRepository
from core.src.repository.email_sender_repository import EmailSenderRepository
from core.src.use_cases.appointment.create import (CreateAppointmentRequest,
                                                   CreateAppointmentResponse)


class CreateAppointment:
    def __init__(
        self,
        appointment_repository: AppointmentRepository,
        email_sender_repository: EmailSenderRepository,
    ):
        self.appointment_repository = appointment_repository
        self.email_sender_repository = email_sender_repository

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

            self.email_sender_repository.send_email_notifications(
                patient_name=appointment.patient_name,
                date=appointment.date,
                time=appointment.time,
                patient_email=appointment.patient_email,
                patient_number=appointment.patient_phone,
            )

            return CreateAppointmentResponse(
                patient_name=appointment.patient_name,
            )

        except AppointmentRepositoryException as e:
            raise AppointmentBusinessException(str(e))

        except EmailSenderRepositoryException as e:
            raise AppointmentBusinessException(str(e))
