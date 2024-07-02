import smtplib
import ssl

import settings.env_variables as env_variables
from adapters.src.exceptions.repository.email_sender import \
    EmailSenderRepositoryException
from adapters.src.repositories.email_sender.mail_templates import (
    client_mail_template, lab_mail_template)
from core.src.repository.email_sender_repository import EmailSenderRepository


class SMTPEmailSenderRepository(EmailSenderRepository):
    def send_email_notifications(
        self,
        patient_name: str,
        date: str,
        time: str,
        patient_email: str,
        patient_number: str,
    ):
        port = int(env_variables.SMTP_PORT)
        smtp_server = str(env_variables.SMTP_SERVER)
        sender_email = str(env_variables.SENDER_EMAIL)
        password = str(env_variables.SENDER_PASSWORD)
        receiver_email = patient_email

        mail_to_client = client_mail_template(
            date=date, time=time, patient_name=patient_name
        )
        mail_to_lab = lab_mail_template(
            date=date,
            time=time,
            patient_name=patient_name,
            patient_number=patient_number,
        )

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, mail_to_client)
                server.sendmail(sender_email, sender_email, mail_to_lab)

        except Exception:
            raise EmailSenderRepositoryException(method="send_email_notifications")
