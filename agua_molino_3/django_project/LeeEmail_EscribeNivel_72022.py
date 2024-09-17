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
            print(" aqui--- ", payload)
            #Content-Type: text/plain; charset="us-ascii"MIME-Version: 1.0Content-Transfer-Encoding: 7bit
            payload1=str(payload).replace('Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\n\n','')
            payload_list.append(str(payload1))
            
        full_body2 = "".join(payload_list)
        #print(full_body2)
except:
    print("No se encontraron correos para leer.")
    
imapSession.expunge()       
imapSession.close()
imapSession.logout()

#************************************************************************
# BORRAR EMAILS
#************************************************************************

#************************************************************************
# FUNCION DE BORRADO DE EMAIL
#************************************************************************
def eraseAllMails():
    import imaplib
    
    username = "Concreto.argos.pa@gmail.com"
    password = 'ypfbkbssvudaqvcl'
    
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, password)

    imapSession.select("INBOX")

    typ, data = imapSession.search(None, 'ALL')
    
    # to get all mails
    status, messages = imapSession.search(None, "ALL")
    
    messages = messages[0].split(b' ')
    for mail in messages:
        _, msg = imapSession.fetch(mail, "(RFC822)")
        imapSession.store(mail, "+FLAGS", "\\Deleted")
        
    imapSession.expunge()
    imapSession.close()
    imapSession.logout()
try:
    eraseAllMails()
    print("Se han borrado todos los correos")
except:
    print("No se encontraron correos para borrar.")

import ast
tabla = []
for j in range(len(payload_list)):
    #print(payload_list[j]," tipo de dato: ", type(payload[j]))
    lil=ast.literal_eval(str(payload_list[j]))
    print(lil)
    tabla=tabla+lil

#************************************************************************
# ESCRITURA EN LA BASE DE DATOS (ValoresSensores)
#************************************************************************
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import types
engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')

for i in range(int(len(tabla))):
    df = pd.DataFrame(data = {"Nivel": [tabla[i]["Nivel"]], "nombre_Silo": [tabla[i]["nombre_Silo"]], "Fecha": [tabla[i]["Fecha"]], "Origen": [tabla[i]["Origen"]], "Hora": [tabla[i]["Hora"]], "Descripcion": [tabla[i]["Descripcion"]]})
    df.to_sql('ValoresSensores', engine, if_exists='append', index = False, )

#************************************************************************
# ESCRITURA EN LA BASE DE DATOS (MorteroSeco)
#************************************************************************
import pandas as pd
import math
from sqlalchemy import create_engine
from sqlalchemy import types
engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')
df2 = pd.read_sql_table('components_silosml', engine)
max_alturas = df2['altura_maxima'][0]
origen_deseado = "Argos Mortero Seco 2060"

cantidad_iter = len(tabla)
k = 1
while k <= 2:
    for i in reversed(tabla):
        if k > 2:
            print("BREAK FOR")
            break
        if i["Origen"] == origen_deseado and i["nombre_Silo"] == "Silo 1":
            print(k,i)
            print("IN SILO 1")
            metrosPrcnt = ((i["Nivel"])*100)/max_alturas
            metrosPrcnt = math.ceil(metrosPrcnt)
            sql_update_query = f"""Update components_silosml set nivel = {metrosPrcnt} where id = 1"""
            engine.execute(sql_update_query)

            sql_update_query = f"""Update components_silosml set metros = {i["Nivel"]} where id = 1"""
            engine.execute(sql_update_query)
            k += 1
        elif i["Origen"] == origen_deseado and i["nombre_Silo"] == "Silo 2":
            print(k,i)
            print("IN SILO 2")
            metrosPrcnt = ((i["Nivel"])*100)/max_alturas
            metrosPrcnt = math.ceil(metrosPrcnt)
            sql_update_query = f"""Update components_silosml set nivel = {metrosPrcnt} where id = 2"""
            engine.execute(sql_update_query)

            sql_update_query = f"""Update components_silosml set metros = {i["Nivel"]} where id = 2"""
            engine.execute(sql_update_query)
            k += 1
        # End of for loop
    print("BREAK WHILE")
    break

#************************************************************************
# ESCRITURA EN LA BASE DE DATOS (Concreto Tocumen)
#************************************************************************
import pandas as pd
import math
from sqlalchemy import create_engine
from sqlalchemy import types
engine = create_engine('postgresql://mantenimiento:#Argos2017@localhost:5432/cemento')
df2 = pd.read_sql_table('components_silos', engine)
max_alturas = df2['altura_maxima'][0]
origen_deseado = "Argos Concreto Tocumen"

cantidad_iter = len(tabla)
k = 1
while k <= 3:
    for i in reversed(tabla):
        if k > 3:
            print("BREAK FOR")
            break
        if i["Origen"] == origen_deseado and i["nombre_Silo"] == "Silo 1":
            print(k,i)
            print("IN IF SILO 1")
            metrosPrcnt = ((i["Nivel"])*100)/max_alturas
            metrosPrcnt = math.ceil(metrosPrcnt)
            sql_update_query = f"""Update components_silos set nivel = {metrosPrcnt} where id = 1"""
            engine.execute(sql_update_query)

            sql_update_query = f"""Update components_silos set metros = {i["Nivel"]} where id = 1"""
            engine.execute(sql_update_query)
            k += 1
        elif i["Origen"] == origen_deseado and i["nombre_Silo"] == "Silo 2":
            print(k,i)
            print("IN IF SILO 2")
            metrosPrcnt = ((i["Nivel"])*100)/max_alturas
            metrosPrcnt = math.ceil(metrosPrcnt)
            sql_update_query = f"""Update components_silos set nivel = {metrosPrcnt} where id = 2"""
            engine.execute(sql_update_query)

            sql_update_query = f"""Update components_silos set metros = {i["Nivel"]} where id = 2"""
            engine.execute(sql_update_query)
            k += 1
        elif i["Origen"] == origen_deseado and i["nombre_Silo"] == "Silo 3":
            print(k,i)
            print("IN IF SILO 3")
            metrosPrcnt = ((i["Nivel"])*100)/max_alturas
            metrosPrcnt = math.ceil(metrosPrcnt)
            sql_update_query = f"""Update components_silos set nivel = {metrosPrcnt} where id = 3"""
            engine.execute(sql_update_query)

            sql_update_query = f"""Update components_silos set metros = {i["Nivel"]} where id = 3"""
            engine.execute(sql_update_query)
            k += 1
        # End of for loop
    print("BREAK WHILE")
    break