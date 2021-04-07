'''import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='iamvj2011@gmail.com',
    to_emails='thalapathiv6@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)'''

'''
import smtplib

email_user = 'iamvj2011@gmail.com'
email_send = 'thalapathiv6@gmail.com'
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
msg = 'test'
server.login(email_user,'one1two2three3')

server.sendmail(email_user,email_send,msg)
server.quit()

'''
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
def mSend():
    print("In mail module")
    email_user = 'iamvj2011@gmail.com'
    email_password = 'one1two2three3'
    email_send = 'thalapathiv6@gmail.com'

    subject = 'Thread Image'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Alert! sombody found'
    msg.attach(MIMEText(body,'plain'))

    filename='img0.jpg'
    attachment  =open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)


    server.sendmail(email_user,email_send,text)
    print("mail sent..")
    server.quit()
