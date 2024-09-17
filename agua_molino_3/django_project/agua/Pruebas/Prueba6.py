import smtplib

sFrom = 'jorge.igg@gmail.com'
sPassword = ''
sTo = 'jorge.garciag@hotmail.com'
sSMTPServer = 'smtp.gmail.com'
nPuerto = 587

sAsunto = 'Hola mundo'
sCuerpo = '''Cuerpo del mensaje.
Saludos
Yo mismo JORGE'''

msg = ("From: %s\r\n" %sFrom)
msg = msg + ('Subject: %s\r\n\r\n' %sAsunto)
msg = msg + sCuerpo

correo = smtplib.SMTP(sSMTPServer,nPuerto,timeout=120)
correo.login(sFrom,sPassword)
resultado = correo.sendmail(sFrom,sTo,msg)
print(resultado)
correo.quit()