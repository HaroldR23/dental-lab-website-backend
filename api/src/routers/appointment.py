from fastapi import APIRouter

from api.src.dtos import Appointment
from core.src.exceptions.business.appointment import (
    AppointmentAlreadyExistsException, BusinessException)
from core.src.use_cases.appointment import CreateAppointmentRequest
from factories.use_cases.appointment import (create_appointment_use_case,
                                             get_all_appointments_use_case)

from .index import index_router

appointment_router = APIRouter()


@appointment_router.post("/appointments", tags=["appointments"])
async def create_appointment(appointment: Appointment):
    try:
        request = CreateAppointmentRequest(
            date=appointment.date,
            time=appointment.time,
            patient_name=appointment.patient_name,
            patient_email=appointment.patient_email,
            patient_phone=appointment.patient_phone,
        )
        use_case = create_appointment_use_case()
        response_use_case = use_case(request=request)
        return response_use_case

    except AppointmentAlreadyExistsException as e:
        raise e
    except BusinessException as e:
        raise e


@appointment_router.get("/appointments", tags=["appointments"])
async def get_all_appointments():
    try:
        use_case = get_all_appointments_use_case()
        response_use_case = use_case()
        appointments = response_use_case.appointments
        return (
            [appointment._asdict() for appointment in appointments]
            if len(appointments) > 0
            else []
        )

    except BusinessException as e:
        raise e


index_router.include_router(appointment_router)
