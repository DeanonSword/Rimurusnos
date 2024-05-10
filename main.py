import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
from tqdm import tqdm

def sendemail(senderemail, senderpassword, recipientemail, subject, messagetext, attachments=None):
    try:
        server = smtplib.SMTP('smtp.mail.ru', 587)
        server.starttls()
        server.login(senderemail, senderpassword)

        message = MIMEMultipart()
        message['From'] = senderemail
        message['To'] = recipientemail
        message['Subject'] = subject

        body = messagetext
        message.attach(MIMEText(body, 'plain'))

        

        server.send_message(message)
        now = datetime.datetime.now()
        print(f"[{now.strftime('%H:%M:%S')}] Письмо от {senderemail} успешно отправлено на {recipientemail}.")

        server.quit()
    except Exception as e:
        print(f"Ошибка при отправке письма: {str(e)}")



logo = """
_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_+_
owner by RIMURU & Paranormal Liberation
        все кроме нас.
        а чë сразу мы?

"""


    
    with open("mail.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            email, password = line.strip().split(":")
            senders.append((email, password))

    print(logo)
    subject = str(input("[AC] название письма > "))
    messagetext = str(input("[AC] текст письма > "))

    for senderemail, senderpassword in senders:
        for recipientemail in recipients:
            sendemail(senderemail, senderpassword, recipientemail, subject, messagetext)
            for _ in tqdm(range(100)):
                pass
