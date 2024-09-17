""" # Import datetime  
from datetime import date, datetime, timedelta

# Local Models de la BD

now = datetime.now() # current date and time UTC
hoy = now.strftime("%Y-%m-%d")
oldday = now - timedelta(days=45)  # day subtraction operation
limite = oldday.strftime("%a, %d %b %Y %H:%M:%S GMT %Z")
print(now)
print(hoy)
print(oldday)
print(limite) """
# ******************************************************************
# -*- coding: utf-8 -*-
# Consulta Basica de una Base de Datos ya creada en PostgreSQL
# Prog. para 
# Import PostgreSQL
import psycopg2
# Import datetime  
from datetime import date, datetime, timedelta, timezone

# Conexion a tu base de datos
# Usa el método conectar()
try:
    credenciales = {
        "dbname": "cemento",
        "user": "mantenimiento",
        "password": "#Argos2017",
        "host": "localhost",
        "port": ''
    }
    cnxn1 = psycopg2.connect(**credenciales)   
    cursor1 = cnxn1.cursor()

    #print("Iniciado PostgreSQL.....")
    # Declaro variables
    colu0 = list()
    colu1 = list()
    colu2 = list()
    colu3 = list()
    colu4 = list()
    listx = ''
    listy = ''    
    # Determinar el ano actual
    now = date.today() # current date and time
    year = date.today().year # current year
    month = date.today().month # current month
    day = date.today().day # current day
    week = date.today().isocalendar()[1] # current weeek from year
    semana = 23
    ano = 1
    # print(now)
    print(year)
    # print(month)
    # print(day)
    # print(week)
    # Determinar si el ano es valido
    if ano:
        if ano == 1 and year > 2023:
            datoyear = year - 1
        else:
            datoyear = year
    else:
        datoyear = year
    print (datoyear)
    # Determinar si se cargo un numero de semana del ano en curso
    if semana:
        if datoyear == 2023 and semana < 22:
            datoweek = week
        elif datoyear == 2023 and semana > 22 and semana <= week:
            datoweek = int(semana)   
        elif datoyear == year and semana <= week and semana in range(1,52):
            datoweek = int(semana)
        elif datoyear > 2023 and datoyear < year and semana in range(1,52):
            datoweek = int(semana)
        else:
            datoweek = week
    else:
        datoweek = week
    print(datoweek)
    # Crear el texto del Query   
    texto_query1 = """
    SELECT MIN(fecha) FROM public."ViewAguaLanzasM3Day"
    WHERE year = %s AND week = %s
    """ % (year, datoweek)
    # Ejecutar una consulta
    cursor1.execute(texto_query1)
    # Se busca la fecha del dia anterior a esta semana 
    while 1:
        row = cursor1.fetchone()
        #print(row) 
        if not row:
            break      
        daytxt = row[0].strftime("%Y-%m-%d")
        #print(daytxt) # day min weed
        fechaold = datetime.strptime(daytxt,"%Y-%m-%d") - timedelta(days=1)  # day subtraction operation
        #print(fechaold)
        datofecha = fechaold.strftime("%Y-%m-%d") # old date
        #print(datofecha)

    # Crear el texto del Query   
    texto_query1 = """
    SELECT MAX(fecha), MAX(volumen) FROM public."ViewAguaLanzasM3Day"
    WHERE TO_CHAR (fecha:: DATE, 'yyyy-mm-dd') <= TO_CHAR ('/%s/':: DATE, 'yyyy-mm-dd')
    """ % (datofecha)
    # Ejecutar una consulta
    cursor1.execute(texto_query1)
    # Se carga a una variable el acumulado del dia anterior
    acum = 0 
    while 1:
        row = cursor1.fetchone()
        #print(row) 
        if not row:
            break 
        acum = int(row[1])
        #print(int(row[1]))
    #print(acum)
    # Crear el texto del Query   
    texto_query1 = """
    SELECT fecha, volumen FROM public."ViewAguaLanzasM3Day"
    WHERE year = %s AND week = %s
    """ % (year, datoweek)
    # Ejecutar una consulta
    cursor1.execute(texto_query1)

    # Se crea la lista de los datos
    ctto = 0
    dato = 0  
    while 1:
        row = cursor1.fetchone()
        #print(row)
        ctto = ctto + 1
        if not row:
            break
        if ctto == 1:
            dato = acum
            colu0.append(row[0].strftime("%Y-%m-%d")) # datetime
            colu1.append(int(row[1])) # volumen
            colu2.append(int(row[1]) - dato) # acumulado
            #print(row[0].weekday())
            if row[0].weekday() == 0:
                colu3.append('LUNES - ')
            elif row[0].weekday() == 1:
                colu3.append('MARTES - ')
            elif row[0].weekday() == 2:
                colu3.append('MIERCOLES - ')            
            elif row[0].weekday() == 3:
                colu3.append('JUEVES - ')
            elif row[0].weekday() == 4:
                colu3.append('VIERNES - ')
            elif row[0].weekday() == 5:
                colu3.append('SABADO - ') 
            elif row[0].weekday() == 6:
                colu3.append('DOMINGO - ')
            dato = int(row[1])
        else:
            colu0.append(row[0].strftime("%Y-%m-%d")) # datetime
            colu1.append(int(row[1])) # volumen
            colu2.append(int(row[1]) - dato) # acumulado
            #print(row[0].weekday())
            if row[0].weekday() == 0:
                colu3.append('LUNES - ')
            elif row[0].weekday() == 1:
                colu3.append('MARTES - ')
            elif row[0].weekday() == 2:
                colu3.append('MIERCOLES - ')            
            elif row[0].weekday() == 3:
                colu3.append('JUEVES - ')
            elif row[0].weekday() == 4:
                colu3.append('VIERNES - ')
            elif row[0].weekday() == 5:
                colu3.append('SABADO - ') 
            elif row[0].weekday() == 6:
                colu3.append('DOMINGO - ')                                                  
            dato = int(row[1])            
    print(colu0,colu1,colu2,colu3)
    # Creo las listas X y Y
    for i in zip(reversed(colu0),reversed(colu3)):
        if listx == '':
            listx = str(i[1]) + str(i[0]) 
        else:
            listx = str(i[1]) + str(i[0]) + ',' + listx

    for i in reversed(colu2):
        if listy == '':
            listy = str(i)
        else:
            listy = str(i) + ',' + listy
    print(listx)
    print(listy)

except Exception as e: 
    #print("Error de conexión PostgreSQL: ", e)
    cursor1.close()  
    cnxn1.close()
finally:
    # Se cierra la conexion SQL y la conexion al Servidos
    cursor1.close()  
    cnxn1.close()
    #print("La conexión PostgreSQL está cerrada")


