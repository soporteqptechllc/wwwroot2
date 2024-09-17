# -*- coding: utf-8 -*-
"""
Creado en Febrero 26 de 2023

@author: Alejandro Alvarado
"""
import os, django
import datetime

from components.models import planta, silosML, silos, pedidos, Valoressensores, llegadas

#Conexion con la base de datos de DJANGO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skote.settings")
django.setup()


day     = datetime.date.today().day
year    = datetime.date.today().year
month   = datetime.date.today().month

#Concretos ARGOS Tocumen, Lee la base de datos de Cada Silo
sensores = Valoressensores.objects.filter(fecha__gte='2023-02-26')
silo21_2=silos.objects.get(pk=1)
silo21_3=silos.objects.get(pk=2)
silo25_3=silos.objects.get(pk=3)

for i in sensores:
    print(sensores.fecha)
"""
if silo21_2.metros < setpoint21_2:
    nombre_cemento = silo21_2.codigo_sap
    cantidad = 27
    unidad = 'ton'
    planta ='Planta de Concretos Tocumen'
    Codigo_SAP_de_cliente = 221
    Codigo_de_producto = silo21_2.codigo_sap
    Cantidad_de_toneladas = cantidad
    Incoterm_entrega ='Entrega'
    Fecha_de_entrega = f"{day}/{month}/{year}"
    Numero_del_silo = 'Silo 21-2'
    
    subject = f"PRIORITARIO: PEDIDO POR GENERACIÓN AUTOMÁTICA DE GRANEL {day}/{month}/{year}"
    l1 = f"PRIORITARIO: PEDIDO POR GENERACIÓN AUTOMÁTICA DE GRANEL {day}/{month}/{year}  Planta: {planta}\n"
    l2 = f"\n"
    l3 = f"Código SAP de cliente     : {Codigo_SAP_de_cliente}\n"
    l4 = f"Código de producto        : {Codigo_de_producto}\n"
    l5 = f"Cantidad de toneladas     : {Cantidad_de_toneladas}\n"
    l6 = f"Incoterm: entrega o retira: {Incoterm_entrega}\n"
    l7 = f"Fecha de entrega          : {Fecha_de_entrega}\n"
    l8 = f"Número del silo           : {Numero_del_silo}\n"
    l9 = f"Nivel Actual Silo (%)      : {silo21_2.nivel}\n"
    l10 = f"Nivel Actual Toneladas (ton) : {silo21_2.toneladas} ton \n"
    body = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10




material = silo21_2.codigo_sap
print(material, silo21_2.codigo_sap)

"""
#po = pedidos(pedidos_id=101,codigo_sap=4526026,description='HE',toneladas=28.8,nivel_porcen=14.5 ,nivel_metros=2.34,estado_pedido=1,fecha_pedido="2022-05-27")
#po.save()
#pedidos.objects.filter(id=3).delete()
#print(pedidos.objects.order_by('fecha_pedido').first()
