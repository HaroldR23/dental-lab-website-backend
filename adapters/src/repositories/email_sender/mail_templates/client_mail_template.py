def client_mail_template(date: str, time: str, patient_name: str) -> str:
    # flake8: noqa: E501
    return f"""
        Hola {patient_name}, esperamos que te encuentres bien, te hablamos del laboratorio dental Pretty Dent para informarte que tu cita ha sido agendada con exito.                
        Datos de la cita:
            Fecha: {date}
            Hora: {time}
            Lugar:  Calle 2a Sur # 30B-118 - Mza 1 Casa 11B - Bosques de Rosa Blanca

        Cita sujeta a cambios, si es necesario nos comunicaremos para informartelo.
    """
