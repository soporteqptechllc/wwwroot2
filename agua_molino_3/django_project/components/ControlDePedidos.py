# -*- coding: utf-8 -*-
"""
Creado en Mayo 26 de 2022
Programa para hacer pedidos de cemento a ArgosOne en funcion del nivel de los silos
-. Guardar los pedidos en la tabla "components_pedidos" esta tabla contiene hasta 5 pedidos por silo y contiene todos los pedidos realizados por este sistema.
    La idea es que al generar un pedido se escribe en la base de datos components_pedidos y si llega una botella a ese silo se marca el pedido mas viejo como entregado
    la base de datos guarda los pedidos abiertos y cerrados historicos.
    
@author: Alejandro Alvarado
"""

#print('Procediendo...')

import email
import imaplib
#import pandas as pd
#from sqlalchemy import create_engine

userName = 'Concreto.argos.pa@gmail.com'
passwd = '#Argos2017'
#directory = "C:/Users/akual/Downloads"

imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login(userName, passwd)

imapSession.select("INBOX")

typ, data = imapSession.search(None, 'ALL')

data = data[0].split(b' ')
try:
    num = 0
    payload_list = []
    for msgId in data:
        #print(msgId)
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
    
        emailBody = messageParts[0][1]
        emailBody = emailBody.decode('utf-8')
        mail = email.message_from_string(emailBody)
        for payload in mail.get_payload():
            payload_list.append(payload)
        full_body = "".join(payload_list)
        print(full_body)
except:
    print("No se encontraron correos para leer.")
    
imapSession.expunge()       
imapSession.close()
imapSession.logout()

def eraseAllMails():
    import imaplib
    
    username = "Concreto.argos.pa@gmail.com"
    password = "#Argos2017"
    
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

try:
    eraseAllMails()
    print("Se han borrado todos los correos")
except:
    print("No se encontraron correos para borrar.")

######################################################

try:
    full_body = full_body.split("\r\n")
    del full_body[-1]
    for i in full_body:
        if "Silo 1: " in i:
            i = i.replace("Silo 1: ", "")
            full_body[0] = i
        if "Silo 2: " in i:
            i = i.replace("Silo 2: ", "")
            full_body[1] = i
        if "Silo 3: " in i:
            i = i.replace("Silo 3: ", "")
            full_body[2] = i
        if "Fecha: " in i:
            i = i.replace("Fecha: ", "")
            full_body[3] = i
        if "Origen: "in i:
            i = i.replace("Origen: ", "")
            full_body[4] = i
        if "Cantidad de Silos: "in i:
            i = i.replace("Cantidad de Silos: ", "")
            full_body[5] = i
        if "Descripcion: "in i:
            i = i.replace("Descripcion: ", "")
            full_body[6] = i

    print(full_body)
except:
    print("No hay correos")

######################################################
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import types
engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')
df2 = pd.read_sql_table('components_silos', engine)
print('df2:')
print(df2['metros'][0])


cantidad_silos = int(full_body[5])
for i in range(cantidad_silos):
    nombre_silo = "Silo "+str(i+1)
    df = pd.DataFrame(data = {"Nivel": [full_body[i]], "nombre_Silo": [nombre_silo], "Fecha": [full_body[3]], "Origen": [full_body[4]], "Hora": [full_body[3]], "Descripcion": [full_body[6]]})
    df.to_sql('ValoresSensores', engine, if_exists='append', index = False, )
    df2['metros'][i]=float(full_body[i])

    print(df2['metros'][0])
    d1=  df2['metros'][0]
    sql_update_query = f"""Update components_silos set metros = {full_body[i]} where id = {i+1}"""
    engine.execute(sql_update_query)

######################################################


#cantidad_silos = int(full_body[5])

#import psycopg2

#for i in range(cantidad_silos):
#    connection = psycopg2.connect(user="mantenimiento",
#                                    password="#Argos2017",
#                                    host="localhost",
#                                    port="5432",
#                                    database="cemento")

#   cursor = connection.cursor()

    # Update single record now
#    print(full_body[i])
#    sql_update_query = """Update components_silos set metros = {full_body[i]} where index = {i}"""
#    connection.commit()
#    count = cursor.rowcount

#    cursor.close()
#    connection.close()

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 13:34:10 2022

@author: akual
"""

#print('Procediendo...')

import email
import imaplib
#import pandas as pd
#from sqlalchemy import create_engine

userName = 'Concreto.argos.pa@gmail.com'
passwd = '#Argos2017'
#directory = "C:/Users/akual/Downloads"

imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
typ, accountDetails = imapSession.login(userName, passwd)

imapSession.select("INBOX")

typ, data = imapSession.search(None, 'ALL')

data = data[0].split(b' ')
try:
    num = 0
    payload_list = []
    for msgId in data:
        #print(msgId)
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
    
        emailBody = messageParts[0][1]
        emailBody = emailBody.decode('utf-8')
        mail = email.message_from_string(emailBody)
        for payload in mail.get_payload():
            payload_list.append(payload)
        full_body = "".join(payload_list)
        print(full_body)
except:
    print("No se encontraron correos para leer.")
    
imapSession.expunge()       
imapSession.close()
imapSession.logout()

def eraseAllMails():
    import imaplib
    
    username = "Concreto.argos.pa@gmail.com"
    password = "#Argos2017"
    
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

try:
    eraseAllMails()
    print("Se han borrado todos los correos")
except:
    print("No se encontraron correos para borrar.")

######################################################

try:
    full_body = full_body.split("\r\n")
    del full_body[-1]
    for i in full_body:
        if "Silo 1: " in i:
            i = i.replace("Silo 1: ", "")
            full_body[0] = i
        if "Silo 2: " in i:
            i = i.replace("Silo 2: ", "")
            full_body[1] = i
        if "Silo 3: " in i:
            i = i.replace("Silo 3: ", "")
            full_body[2] = i
        if "Fecha: " in i:
            i = i.replace("Fecha: ", "")
            full_body[3] = i
        if "Origen: "in i:
            i = i.replace("Origen: ", "")
            full_body[4] = i
        if "Cantidad de Silos: "in i:
            i = i.replace("Cantidad de Silos: ", "")
            full_body[5] = i
        if "Descripcion: "in i:
            i = i.replace("Descripcion: ", "")
            full_body[6] = i

    print(full_body)
except:
    print("No hay correos")

######################################################
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import types
engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')
df2 = pd.read_sql_table('components_silos', engine)
print('df2:')
print(df2['metros'][0])


cantidad_silos = int(full_body[5])
for i in range(cantidad_silos):
    nombre_silo = "Silo "+str(i+1)
    df = pd.DataFrame(data = {"Nivel": [full_body[i]], "nombre_Silo": [nombre_silo], "Fecha": [full_body[3]], "Origen": [full_body[4]], "Hora": [full_body[3]], "Descripcion": [full_body[6]]})
    df.to_sql('ValoresSensores', engine, if_exists='append', index = False, )
    df2['metros'][i]=float(full_body[i])

    print(df2['metros'][0])
    d1=  df2['metros'][0]
    sql_update_query = f"""Update components_silos set metros = {full_body[i]} where id = {i+1}"""
    engine.execute(sql_update_query)

######################################################


#cantidad_silos = int(full_body[5])

#import psycopg2

#for i in range(cantidad_silos):
#    connection = psycopg2.connect(user="mantenimiento",
#                                    password="#Argos2017",
#                                    host="localhost",
#                                    port="5432",
#                                    database="cemento")

#   cursor = connection.cursor()

    # Update single record now
#    print(full_body[i])
#    sql_update_query = """Update components_silos set metros = {full_body[i]} where index = {i}"""
#    connection.commit()
#    count = cursor.rowcount

#    cursor.close()
#    connection.close()

