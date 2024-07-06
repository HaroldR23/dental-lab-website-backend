from fastapi import APIRouter, HTTPException

from api.src.dtos import Appointment
from api.src.routers.index import index_router
from core.src.use_cases.appointment.create import CreateAppointmentRequest
from factories.use_cases.appointment import (create_appointment_use_case,
                                             get_all_appointments_use_case)

appointment_router = APIRouter()


@appointment_router.post("/appointments", tags=["appointments"])
async def create_appointment(appointment: Appointment):
    try:
        request = CreateAppointmentRequest(
            date=appointment.date,
            time=appointment.time,
            patient_name=appointment.patient_name,
            patient_email=appointment.patient_email,
        )
        use_case = create_appointment_use_case()
        response_use_case = use_case(request=request)
        return response_use_case
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


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
    except Exception as e:
        raise HTTPException(status_code=500, detail={"message": str(e)})


index_router.include_router(appointment_router)
