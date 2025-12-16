# checker/email_notifier.py

import smtplib
from email.message import EmailMessage
import os

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL_FROM = os.environ["EMAIL_FROM"]
EMAIL_TO = os.environ["EMAIL_TO"]
EMAIL_PASSWORD = os.environ["EMAIL_PASSWORD"]

def send_email(subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.set_content(body)

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)
