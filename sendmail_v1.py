# -*- coding: utf-8 -*-

import smtplib
from time import sleep
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from string import Template

def read_template(filename):
    with open(filename, mode='r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

try:
    cont = 0
    nombre_destino = 'Usuario'
    destino = 'ranchaluisa@devoxs.com'
    host = 'smtp-mail.outlook.com'
    port = 587
    remitente = 'joinic2@hotmail.com'
    #clave = 'passwordsecreto'
    clave = 'thebest2'

    asunto = 'Envio de mail desde Python'
    path_template_m = 'message.txt'

    message_template = read_template(path_template_m)

    print ('\nLogin: {}' . format(host))
    server = smtplib.SMTP(host,port)
    server.starttls()
    server.login(remitente,clave)

    msg = MIMEMultipart()
    body = message_template.substitute(PERSON_NAME=nombre_destino)
    msg['From'] = remitente
    msg['To'] = destino
    msg['Subject'] = asunto
    msg.attach(MIMEText(body,'plain'))

    print ('\nSending message, Please wait...')
    cont += 1
    server.sendmail(remitente,destino,msg.as_string())
    print('Sent {}: {} - OK' . format(cont,destino))
    status_close_mail = server.quit()
    print ('\nComplete!! :)\n')
except KeyError:
    print (':( Error trying send mail!!\n')    