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
import numpy as np
import datetime
pd.set_option('mode.chained_assignment', None)

#df = pd.DataFrame(list(BlogPost.objects.all().values()))



def tablaBotellas(tabla):
    # Cambia el contenido del campo fecha del Dataframe de tabla a fecha y hora tipo datatime
    ix = 0
    for i in tabla['fecha']:
        tabla['fecha'][ix]=pd.to_datetime(str(i)+" "+str(tabla['hora'][ix]))
        ix=ix+1
    tablanp = np.array(tabla['nivel'], tabla['fecha'])
    tabnpdiff = np.diff(tablanp)
    print(np.mean(tabnpdiff))
    for i in tabnpdiff:
        if i>5:
            print(i)



    return True
########

#dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-2').values()))
#tablaBotellasSilo21_2 = tablaBotellas(dfSilo)

#dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-3').values()))
#tablaBotellasSilo21_3 = tablaBotellas(dfSilo)

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 25-3').values()))
tablaBotellasSilo25_3 = tablaBotellas(dfSilo)
