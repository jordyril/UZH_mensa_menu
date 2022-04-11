import os
import smtplib
from datetime import date
from email.message import EmailMessage

from general import URLS, WORKDAYS
from day import Day
from util import box

EMAIL_ADDRESS = os.environ.get("GMAIL_USER")
EMAIL_PASSWORD = os.environ.get("GMAIL_PASS")

RECEIVER = "jordy.rillaerts@bf.uzh.ch"

body = ""
for d in WORKDAYS:
    body += box(d.upper())
    body += Day(d, URLS[:6]).summary
    body += "\n \n \n"

# basic email parameters
today = date.today()
week_nbr = today.isocalendar()[1]

subject = f"Mensa plan for week {week_nbr}"

### set up message with EmailMessage
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
