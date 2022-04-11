import os
import smtplib
from datetime import date
from email.message import EmailMessage

from general import DAYS, URLS, WORKDAYS
from day import Day

EMAIL_ADDRESS = os.environ.get("GMAIL_USER")
EMAIL_PASSWORD = os.environ.get("GMAIL_PASS")

RECEIVER = "jordy.rillaerts@bf.uzh.ch"

# look up todays menu
my_date = date.today()
today = DAYS[my_date.weekday()]

if today in WORKDAYS:
    mensas_day = Day(today, URLS[:6])

    # basic email parameters
    subject = f"Mensa plan for {today} {my_date}"
    body = mensas_day.summary

    # set up message with EmailMessage
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = RECEIVER
    msg.set_content(body)

    # msg.add_alternative(
    #     """
    # <!DOCTYPE html>
    # <html>
    #     <body>
    #         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    #     </body>
    # </html>
    # """,
    #     subtype="html",
    # )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
