from typing import List
from unittest.mock import patch

from fastapi.testclient import TestClient

from core.src.exceptions.business.appointment import (
    AppointmentAlreadyExistsException, AppointmentBusinessException)
from core.src.models.appointment import Appointment
from core.src.use_cases.appointment.create import CreateAppointment
from core.src.use_cases.appointment.get_all import (GetAllAppointments,
                                                    GetAllAppointmentsResponse)


def test_create_appointment_successfully(
    client: TestClient, mock_appointment_payload: dict
):
    mock_response_use_case = {"name": "Appointment 1"}
    with patch.object(
        CreateAppointment, "__call__", return_value=mock_response_use_case
    ):
        response = client.post("/appointments", json=mock_appointment_payload)
        assert response.status_code == 200
        assert response.json() == mock_response_use_case


def test_create_appointment_should_raise_http_exception_when_something_went_wrong(
    client: TestClient, mock_appointment_payload: dict
):
    with patch.object(
        CreateAppointment,
        "__call__",
        side_effect=AppointmentAlreadyExistsException(date="27/08/2024", time="10:00"),
    ):
        response = client.post("/appointments", json=mock_appointment_payload)
        assert response.status_code == 409
        assert response.json() == {
            "message": "The Appointment with the date 27/08/2024 and time 10:00 already exists."
        }


def test_get_all_appointments_should_return_an_empty_list_when_there_is_not_appointments(
    client: TestClient,
):
    with patch.object(
        GetAllAppointments,
        "__call__",
        return_value=GetAllAppointmentsResponse(appointments=[]),
    ):
        response = client.get("/appointments")
        assert response.status_code == 200
        assert response.json() == []


def test_get_all_appointments_should_return_a_list_of_appointments(
    client: TestClient, mock_appointments: List[Appointment]
):
    with patch.object(
        GetAllAppointments,
        "__call__",
        return_value=GetAllAppointmentsResponse(appointments=mock_appointments),
    ):
        response = client.get("/appointments")
        assert response.status_code == 200
        assert response.json() == [
            {
                "date": appointment.date,
                "time": appointment.time,
                "patient_name": appointment.patient_name,
                "patient_email": appointment.patient_email,
                "id": appointment.id,
                "patient_phone": appointment.patient_phone,
            }
            for appointment in mock_appointments
        ]


def test_get_all_appointments_should_raise_http_exception_when_something_went_wrong(
    client: TestClient,
):
    with patch.object(
        GetAllAppointments,
        "__call__",
        side_effect=AppointmentBusinessException("Error"),
    ):
        response = client.get("/appointments")
        assert response.status_code == 500
        assert response.json() == {"message": "Error"}
