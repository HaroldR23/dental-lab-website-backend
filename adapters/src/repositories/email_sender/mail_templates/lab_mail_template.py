def lab_mail_template(
    date: str, time: str, patient_name: str, patient_number: str
) -> str:
    # flake8: noqa: E501
    return f"""
            Tenemos una nueva cita agendada, revisar si no se cruza con otro cliente, en dado caso comunicarse con el paciente.
            Datos de la cita:
                Nombre del paciente: {patient_name}
                Celular: {patient_number}
                Fecha: {date}
                Hora: {time}
    """
