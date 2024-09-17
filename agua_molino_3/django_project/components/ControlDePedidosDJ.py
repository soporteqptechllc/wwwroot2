# -*- coding: utf-8 -*-
"""
Creado en Mayo 26 de 2022
Programa para hacer pedidos de cemento a ArgosOne en funcion del nivel de los silos
-. Guardar los pedidos en la tabla "components_pedidos" esta tabla contiene hasta 5 pedidos por silo y contiene todos los pedidos realizados por este sistema.
    La idea es que al generar un pedido se escribe en la base de datos components_pedidos y si llega una botella a ese silo se marca el pedido mas viejo como entregado
    la base de datos guarda los pedidos abiertos y cerrados historicos.
    
@author: Alejandro Alvarado
"""

from components.models import pedidos
#from models import silos, pedidos
#from time import gmtime, strftime
#from os import remove

#import datetime
#import os
#po = pedidos.objects.create()
po = pedidos.objects.all().exclude(pk=0)
print(po)