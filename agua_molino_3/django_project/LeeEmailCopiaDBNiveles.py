# -*- coding: utf-8 -*-
"""
Creado en Noviembre 5, 2022
Programa para hacer pedidos de cemento a ArgosOne en funcion del nivel de los silos
-. Guardar los pedidos en la tabla "components_pedidos" esta tabla contiene hasta 5 pedidos por silo y contiene todos los pedidos realizados por este sistema.
    La idea es que al generar un pedido se escribe en la base de datos components_pedidos y si llega una botella a ese silo se marca el pedido mas viejo como entregado
    la base de datos guarda los pedidos abiertos y cerrados historicos.
    
@author: Alejandro Alvarado
"""
#************************************************************************
# CONFIGURACION DE LEER EMAIL
#************************************************************************
import email
import imaplib

userName = 'Concreto.argos.pa@gmail.com'
password = 'ypfbkbssvudaqvcl'
#directory = "C:/Users/akual/Downloads"

imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login(userName, password)

imapSession.select("INBOX")

typ, data = imapSession.search(None, 'ALL')
#************************************************************************
# LECTURA DE EMAIL
#************************************************************************
data = data[0].split(b' ')
try:
    num = 0
    payload_list = []
    for msgId in data:
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')

        emailBody = messageParts[0][1]
        emailBody = emailBody.decode('utf-8')
        mail = email.message_from_string(emailBody)
        for payload in mail.get_payload():
            payload_list.append(str(payload))
        full_body = "".join(payload_list)
except:
    print("No se encontraron correos para leer.")
    
imapSession.expunge()       
imapSession.close()
imapSession.logout()

#************************************************************************
# FUNCION DE BORRADO DE EMAIL
#************************************************************************
def eraseAllMails():
    import imaplib
    
    username = "Concreto.argos.pa@gmail.com"
    password = 'ypfbkbssvudaqvcl'
    
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    
    imap.login(username, password)
    
    imap.select("INBOX")
    
    # to get all mails
    status, messages = imap.search(None, "ALL")
    
    messages = messages[0].split(b' ')
    for mail in messages:
        _, msg = imap.fetch(mail, "(RFC822)")
        imap.store(mail, "+FLAGS", "\\Deleted")
        
    imap.expunge()
    imap.close()
    imap.logout()
#************************************************************************
# BORRAR EMAILS
#************************************************************************
try:
    eraseAllMails()
    print("Se han borrado todos los correos")
except:
    print("No se encontraron correos para borrar.")

#************************************************************************
# LECTURA DEL CONTENIDO DEL EMAIL
#************************************************************************
#Origen: Argos Concreto Tocumen

try:
    full_body = full_body.split("\n")
    FB = []
    for s in full_body:
        if "Nivel" in s:
            s = s.replace("Content-Type: application/octet-stream","")
            s = s.replace('Content-Type: text/plane; charset="us-ascii"',"")
            s = eval(s)
            FB.append(s)
    full_body = FB
    FB = []
    for l in full_body:
        for i in l:
            FB.append(i)
    print("***********************")
    print(FB)
    print(len(FB))
    full_body = FB


    #************************************************************************
    # ESCRITURA EN LA BASE DE DATOS
    #************************************************************************
    import pandas as pd
    from sqlalchemy import create_engine
    from sqlalchemy import types
    engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')
    df2 = pd.read_sql_table('components_silos', engine)
    print('df2:')
    print(df2['metros'])


    for i in full_body:
        nivel = i["Nivel"]
        nombreSilo = i["nombre_Silo"]
        fecha = i["Fecha"]
        origen = i["Origen"]
        hora = i["Hora"]
        descripcion = i["Descripcion"]

        df = pd.DataFrame(data = {"Nivel": [nivel], "nombre_Silo": [nombreSilo], "Fecha": [fecha], "Origen": [origen], "Hora": [hora], "Descripcion": [descripcion]})
        print(df)
        df.to_sql('ValoresSensores', engine, if_exists='append', index = False, )

    #components_silos
    for i in full_body:
        nivel = round(i["Nivel"],2)
        fecha = i["Fecha"]
        porce = round(nivel*10,2) # 10 metros de altura al multiplicarlo por 10 tenemos el porcentaje
        nombreSilo = i["nombre_Silo"]
        origen = i["Origen"] 
        if origen == "Concretos Tocumen":
            sql_update_query = f"""Update components_silos set metros = {float(nivel)}, nivel = {float(porce)}, fecha_estado_silo = '{fecha}' where silo = '{nombreSilo}'"""
            engine.execute(sql_update_query)

    #components_silosml
    for i in full_body:
        nivel = round(i["Nivel"],2)
        porce = round(nivel*100/8,2)
        nombreSilo = i["nombre_Silo"]
        origen = i["Origen"] 
        if origen == "Argos Mortero Seco 2060":
            sql_update_query = f"""Update components_silosml set metros = {float(nivel)}, nivel = {float(porce)}, fecha_estado_silo = '{fecha}' where silo = '{nombreSilo}'"""
            engine.execute(sql_update_query)

except:
    print("No hay correos")