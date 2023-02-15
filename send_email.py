from datetime import datetime
import smtplib 
from datetime import date
from datetime import datetime
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email import encoders
from urllib import response
import requests
import json

def get_credentials():
    f = open('sender_credentials.json')
    data = json.load(f)
    sender = data['sender']
    password = data['token']
    return sender, password
    
def get_content():
    # ainda não sei bem como definir quais emails vão passar por aqui...
    response = requests.get('http://127.0.0.1:8000/{email}')
    receiver = response[0]['email']
    for item in response[0]['schedules']:
        #if condicao de ainda não enviado
        #condicação que condiz com a data do dia
        if item['date'] == datetime.now():
            title = item['title']
            date = item['date']
            content = f'Seu evento {title} começará em {date}'
            subject = date
            print(item)
            send_email(content, subject, receiver)
      
def send_email(content, subject, receiver):
    sender, password = get_credentials()
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    msg.attach(MIMEText(content))
    msg = msg.as_string()
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg)
        server.quit()
        print('enviado')
    except:
        print('erro')
        
if __name__ == '__main__':
    get_content()

