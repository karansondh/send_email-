import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html =Template(Path('index.html').read_text())
email = EmailMessage()
email['from']= 'your.email@gmail.com'
email['to']= 'reciever.email@gmail.com'
email['subject']=  'Email Subject'

email.set_content(html.substitute({'name': 'tintin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('your.email@gmail.com' ,'YOU"R EMAIL PASSWORD')
    smtp.send_message(email)
    print("all good boss!!")
