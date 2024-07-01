from typing import List, NamedTuple

from core.src.models.appointment import Appointment


class GetAllAppointmentsResponse(NamedTuple):
    appointments: List[Appointment]
