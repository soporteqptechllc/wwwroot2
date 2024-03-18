import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''
Hola Mundo ... Prueba (Contenido del correo) !!!
'''

sender_address = 'jorge.igg@gmail.com'
sender_pass = 'bhun njmp zenb urmf'
receiver_address = 'jorge.garciag@hotmail.com'

message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Prueba de envio de correo con Python y Gmail (Titulo)'   

message.attach(MIMEText(mail_content, 'plain'))
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
