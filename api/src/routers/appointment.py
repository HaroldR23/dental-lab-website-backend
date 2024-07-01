from fastapi import APIRouter

from api.src.dtos.appointment_dto import Appointment
from api.src.routers.index import index_router

appointment_router = APIRouter()


@appointment_router.post("/appointments")
async def create_appointment(appointment: Appointment):
    raise NotImplementedError


index_router.include_router(appointment_router)
