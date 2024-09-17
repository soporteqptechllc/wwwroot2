# -*- coding: utf-8 -*-
"""
Creado en Febrero 26 de 2023

@author: Alejandro Alvarado
"""
import os, django
import datetime


#Conexion con la base de datos de DJANGO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skote.settings")
django.setup()
from components.models import silos, pedidos, Valoressensores, llegadas

day     = datetime.date.today().day
year    = datetime.date.today().year
month   = datetime.date.today().month
fecha_ayer = datetime.date.today()-datetime.timedelta(1)

day_ayer = fecha_ayer.day
month_ayer = fecha_ayer.month
year_ayer = fecha_ayer.year

import pandas as pd
import datetime
pd.set_option('mode.chained_assignment', None)

#df = pd.DataFrame(list(BlogPost.objects.all().values()))



def tablaBotellas(tabla):
    """
    identifica si en una curva de nivel de un silo de cemento hay un incremetno de DN_botella metros (1.8 m) en un tiempo mayor a TbotellaMin (40 minutos)
    esto se asume que es un indentificador que una botella lleno el silo.

    Los resultados se guarda en la tabla de llegadas (arrived)

    """
    Nact = 0 # Nivel Actual
    Nmin = 0 # Nivel minimo encontrado
    DN_botella = 1.8 # Delta incremento del Nivel del silo que representa lo que lo subiria una botella.
    TbotellaMin = 40 # minutos minimos que dura una botella en llenar el valor DN_botella
    planta = tabla['origen'][len(tabla)-1]
    nom_silo = tabla['nombre_silo'][len(tabla)-1]
    description = tabla['descripcion'][len(tabla)-1]
    #arrived = pd.DataFrame(list(llegadas.objects.filter(planta==planta, nom_silo == nom_silo).values()))
    last_arrived = llegadas.objects.filter(planta=planta, nom_silo = nom_silo).last()
    try:
        Nmin        = last_arrived.n_minimo
        i_sensor    = last_arrived.id_sensorLL
        tabBot      = last_arrived
    except Exception:
        tabBot      = llegadas(n_minimo = 0.0,planta = planta, nom_silo = nom_silo, description=description)
        Nmin        = 30
        i_sensor    = 1
        tabBot.save()
    
    # Reduce los datos del sensor de nivel a partir del ultimo dato guardado en llegadas
    tabla = tabla[tabla['id']>i_sensor].reset_index(drop=True)

    # Lee el SETPOINT
    setpoint = silos.objects.filter(planta = planta, silo = nom_silo).last().setpoint
    

    # Filtra Pedidos Modelo
    PedidosLibres = True
    try:
        ped = pedidos.objects.filter(planta = planta, nom_silo = nom_silo, id_tablaLlegadas = None).order_by('id_sensorP')


    except Exception as err:
        PedidosLibres = False
        print(err)

    # Cambia el contenido del campo fecha del Dataframe de tabla a fecha y hora tipo datatime
    from django.utils import timezone
    import pytz

    ix = 0
    for i in tabla['fecha']:
        #print(i,tabla['hora'][ix])
        tabla['fecha'][ix]=pd.to_datetime(str(i)+" "+str(tabla['hora'][ix])).replace(tzinfo=pytz.UTC)
        ix=ix+1
        

    
    fechaNula = pd.to_datetime('1971-02-26 00:00:00')

    def deltaOK(lista,i):
        return True

    ##print("inicio de revision de niveles",'/n',tabBot)
    w = 0
    for i in range(len(tabla)):
        #print(i,"Valor actual y valor minimo:", tabla['nivel'][i],Nmin,tabBot.fecha_min,tabBot.n_minimo)
        if tabla['nivel'][i] <= Nmin:
            # print("un menor   ",i,"Valor actual y valor minimo:", tabla['nivel'][i],Nmin)
            if deltaOK(tabla,i):
                Nmin = float(tabla['nivel'][i] )
                tabBot.fecha_min    = tabla['fecha'][i]
                tabBot.fecha_fin    = fechaNula
                tabBot.n_minimo     = float(Nmin)
                tabBot.n_maximo     = 0.0
                tabBot.incremento   = 0.0
                tabBot.id_sensorLL  = int(tabla['id'][i])
                tabBot.save()
            else:
                pass
        else:
            if tabla['nivel'][i]-Nmin >= DN_botella:
                
                fecha1 = tabBot.fecha_min
                fecha2 = tabla['fecha'][i]
                #print(i,"     ",fecha1,"       ",fecha2,"  ",fechaNula)
                diferencia = fecha2 - fecha1
                ##print("i=",i,"w=",w,"fecha2= ",fecha2, "fecha1= ", fecha1, "Delta= ", diferencia)
                if diferencia >= datetime.timedelta(minutes=TbotellaMin):
                    ##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    ##print("        llego una botella")
                    ##print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    Nmin = tabla['nivel'][i] 
                    # Llenad y cierra el registro.
                    tabBot.fecha_fin    = tabla['fecha'][i]
                    tabBot.n_maximo     = tabla['nivel'][i]
                    tabBot.incremento   = tabBot.n_maximo-tabBot.n_minimo
                    tabBot.id_sensorLL  = tabla['id'][i]
                    tabBot.save()
                 
                   
                    # Crea un nuevo registro y lo apuntamos con el mismo nombre
                    tabBot_next = llegadas(planta = planta, nom_silo = nom_silo, description = description)
                    tabBot = tabBot_next
                    # Rellena el nuevo registro con datos pertinentes.
                    tabBot.fecha_min    = tabla['fecha'][i]
                    tabBot.fecha_fin    = fechaNula
                    tabBot.n_minimo     = Nmin
                    tabBot.n_maximo     = 0
                    tabBot.incremento   = 0
                    tabBot.id_sensorLL  = tabla['id'][i]
                    tabBot.save()


                else:
                    pass
            else:
                pass
        
        
    # Empareja los pedidos con las llegadas de botellas en funcion en el orden de llegadas y la secuencias
    # de valores de los sensores.
    from emparejarPedidosLlegadas import emparejar

    if emparejar(planta, nom_silo):
        print(planta, nom_silo)

    return tabBot
########

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-2').values()))
tablaBotellasSilo21_2 = tablaBotellas(dfSilo)

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-3').values()))
tablaBotellasSilo21_3 = tablaBotellas(dfSilo)

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 25-3').values()))
tablaBotellasSilo25_3 = tablaBotellas(dfSilo)
