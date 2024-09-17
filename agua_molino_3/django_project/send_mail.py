"""
Created on Thu Feb 18 16:50:54 2021

@author: aalvarado
"""
def mail(to, subject, filename, file_path):
    """

    Parameters
    ----------
    to : TYPE: string
        DESCRIPTION: Email de destino
        
    subject : TYPE: string
        DESCRIPTION: Asunto del email
        
    filename : TYPE: string
        DESCRIPTION: El nombre del archivo adjunto
        
    file_path : TYPE: string
        DESCRIPTION: La ruta del archivo, incluyendo el nombre del archivo

    Returns: 1
    -------
    None.

    """
    
    
    # send_attachment.py
    #import necessary packages
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.image import MIMEImage
    from email.mime.text import MIMEText
    from email import encoders
    import smtplib
    
    # create message object instance
    msg = MIMEMultipart()
     
    
    # setup the parameters of the message
    password = "timv-ebmh-ddmr-ovmv"
    msg['From'] = "argos.pa@icloud.com"
    msg['To'] = to
    msg['Subject'] = subject
     
    # attach image to message body
    body = 'Buenos días, este es un email de envio automático de Q&P Tech Panama Inc. \n'
    msg.attach(MIMEText(body,'plane'))
    attachment = open(file_path,'rb')
    
    # attach excel file
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)
    
     
     
    # create server
    server = smtplib.SMTP('smtp.mail.me.com: 587')
     
    server.starttls()
     
    # Login Credentials for sending the mail
    server.login(msg['From'], password)
     
     
    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
    return 1