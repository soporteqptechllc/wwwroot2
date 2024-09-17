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

def tablaPedidos(tabla):
    """
    identifica si en una curva de nivel de un silo de cemento hay un decremento de DN_botella metros (2 m) en un tiempo mayor a TbotellaMin (40 minutos)
    esto se asume que es un indentificador para pedir botella.

    Los resultados se guardan en la tabla de pedidos.
    """
    from PedidosTocumen import realizarPedido
    Nmax = 0 # Nivel maximo encontrado
    DN_botella = 1.9 # Delta decremento del Nivel del silo que representa lo que lo subiria una botella.
    
    planta      = tabla['origen'][len(tabla)-1]
    nom_silo    = tabla['nombre_silo'][len(tabla)-1]
    description = tabla['descripcion'][len(tabla)-1]
    last_pedido = pedidos.objects.filter(planta=planta, nom_silo = nom_silo).last()

    try:
        Nmax        = last_pedido.n_maximo
        i_sensor    = last_pedido.id_sensorP
        tabPedido   = last_pedido
    except Exception:
        tabPedido   = pedidos(n_maximo = 0.0, nivel_metros=0, planta = planta, nom_silo = nom_silo,description = description)
        Nmax        = 0
        i_sensor    = 1
        tabPedido.save()
    
    # Reduce los datos del sensor de nivel a partir del ultimo dato guardado en llegadas
    tabla = tabla[tabla['id']>i_sensor].reset_index(drop=True)

    pd.set_option('mode.chained_assignment', None)
    
    # Cambia el contenido del campo fecha del Dataframe de tabla a fecha y hora tipo datatime
    ix = 0
    for i in tabla['fecha']:
        tabla['fecha'][ix]=pd.to_datetime(str(i)+" "+str(tabla['hora'][ix]))
        ix=ix+1

    fechaNula = pd.to_datetime('1971-02-26 00:00:00')

    def deltaOK(lista,i):
        return True
    for i in range(len(tabla)):
        #print(tabla['nivel'][i],Nmax)
        if tabla['nivel'][i] >= Nmax:
            #print("se encontro un mayor")
            if deltaOK(tabla,i):
                Nmax = float(tabla['nivel'][i] )
                tabPedido.fecha_max     = tabla['fecha'][i]
                tabPedido.fecha_pedido  = fechaNula
                tabPedido.nivel_metros  = 0.0
                tabPedido.n_maximo      = float(Nmax)
                tabPedido.decremento    = 0.0
                tabPedido.id_sensorP    = int(tabla['id'][i])
                tabPedido.save()
            else:
                pass
        else:
            if tabPedido.n_maximo-tabla['nivel'][i] >= DN_botella:
                Nmax = tabla['nivel'][i] 
                tabPedido.fecha_pedido  = tabla['fecha'][i]
                tabPedido.nivel_metros  = tabla['nivel'][i]
                tabPedido.decremento    = tabPedido.n_maximo-tabPedido.nivel_metros
                tabPedido.id_sensorP    = tabla['id'][i]
                tabPedido.save()
                realizarPedido("Planta Tocumen",tabPedido.nom_silo,tabPedido.id)


                # Crea un nuevo registro y lo apuntamos con el mismo nombre
                tabPedido_next = pedidos(planta = planta, nom_silo = nom_silo, description = description)
                tabPedido = tabPedido_next
                # Rellena el nuevo registro con datos pertinentes.
                tabPedido.fecha_max     = tabla['fecha'][i]
                tabPedido.fecha_pedido  = fechaNula
                tabPedido.nivel_metros  = 0.0
                tabPedido.n_maximo      = Nmax
                tabPedido.decremento    = 0.0 
                tabPedido.id_sensorP    = tabla['id'][i]
                tabPedido.save()

            else:
                pass


    return True
########

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-2').values()))
tablaPedidosSilo21_2 = tablaPedidos(dfSilo)

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 21-3').values()))
tablaPedidosSilo21_3 = tablaPedidos(dfSilo)

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(2023, 1, 1), nombre_silo ='Silo 25-3').values()))
tablaPedidosSilo25_3 = tablaPedidos(dfSilo)

from CalculoPedidosSP import calculopedido
silo21_2=silos.objects.get(pk=1)
silo21_3=silos.objects.get(pk=2)
silo25_3=silos.objects.get(pk=3)
calculopedido("Concretos Tocumen", silo21_2)
calculopedido("Concretos Tocumen", silo21_3)
calculopedido("Concretos Tocumen", silo25_3)