from unittest.mock import patch

from fastapi.testclient import TestClient

from core.src.use_cases.appointment.create import CreateAppointment


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
    with patch.object(CreateAppointment, "__call__", side_effect=Exception("Error")):
        response = client.post("/appointments", json=mock_appointment_payload)
        assert response.status_code == 500
        assert response.json() == {"detail": {"message": "Error"}}
