import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html =Template(Path('index.html').read_text())
email = EmailMessage()
email['from']= #enter in ''
email['to']= #receiver's email in ''
email['subject']= #enter in ''

email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(#email in '' ,# you'r password in '')
    smtp.send_message(email)
    print("all good boss!!")
