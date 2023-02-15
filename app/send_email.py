import smtplib 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
import requests
import json

# senha N7hOiZ0b
#parametros?
def get_credentials():
    f = open('sender_credentials.json')
    data = json.load(f)
    sender = data['sender']
    password_token = data['token']
    
    response = requests.get(f'api addr/<{id}>') # a ser mudado dependendo da estrutura da api
    receiver = response.json()['receiver']
    return receiver, sender, password_token

def get_content():
    response = requests.get(f'api addr/<{id}>')
    content = response.json()['receiver']
    subject = f"mail subject bla bla"
    return content, subject 

def send_email():
    receiver, sender, password_token = get_credentials()
    content, subject = get_content()
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    #msg.attach(MIMEText(content, 'html')) # if it's html
    msg.attach(MIMEText(content))
    msg = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender, password_token)
        server.sendmail(sender, receiver, msg)
        server.quit()
        return 1
    except:
        return 0
        
if __name__ == '__main__':
    send_email()

