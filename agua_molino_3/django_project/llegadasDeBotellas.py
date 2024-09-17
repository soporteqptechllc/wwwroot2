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

#Concretos ARGOS Tocumen, Lee la base de datos de Cada Silo
sensores = Valoressensores.objects.filter(fecha__gte='2023-02-28')
#silo21_2=silos.objects.get(pk=1)
#silo21_3=silos.objects.get(pk=2)
#silo25_3=silos.objects.get(pk=3)
#print(len(sensores))
#for i in sensores:
#    print(i.fecha, i.origen,i.nivel)

########
import pandas as pd
import datetime
pd.set_option('mode.chained_assignment', None)

#df = pd.DataFrame(list(BlogPost.objects.all().values()))



def tablaBotellas(tabla):

    """
    class llegadas(models.Model):
    llegadas_id          =   models.BigIntegerField(db_column='llegadas_id', blank=True, null=True)            # id de pedido
    description         =   models.TextField(db_column='description', blank=True, null=True)                # Informacion del pedido
    nivel_porcen        =   models.FloatField(db_column='nivel_porcen', blank=True, null=True)              # Porcentaje de Nivel al momento de generla el pedido
    fecha_fin           =   models.DateTimeField(db_column='fecha_fin', blank=True, null=True)           # Fecha se genero el pedido.
    n_maximo            =   models.FloatField(db_column='nivel_maximo', blank=True, null=True)              # Valor maximo punto de partida de la medicion.
    n_minimo            =   models.FloatField(db_column='nivel_minimo', blank=True, null=True)              # Valor maximo punto de partida de la medicion.
    incremento          =   models.FloatField(db_column='incremento', blank=True, null=True)                # Valor que define la botella. Diferencia entre el maximo y minimo
    fecha_min           =   models.DateTimeField(db_column='fecha_min', blank=True, null=True)              # Fecha del punto de inicio de la medicion Valor maximo
    id_sensorLL         =   models.BigIntegerField(db_column='sensor_id', blank=True, null=True)

    """
    Nact = 0 # Nivel Actual
    Nmin = 0 # Nivel minimo encontrado
    DN_botella = 1.8 # Delta incremento del Nivel del silo que representa lo que lo subiria una botella.
    TbotellaMin = 40 # minutos minimos que dura una botella en llenar el valor DN_botella
    fila = ['1971-02-26 00:00:00','1971-02-26 00:00:00',12.0,0.0,0.0]
    tabBot = pd.DataFrame([fila],columns=['fecha_min','fecha_fin','N_minimo','N_maximo','incremento'])
    tabBot['fecha_min'] = pd.to_datetime(tabBot['fecha_min'])
    tabBot['fecha_fin'] = pd.to_datetime(tabBot['fecha_fin'])
    filaNula = tabBot
    ix = 0
    #tabla['fecha']=pd.to_datetime(tabla['fecha'])
    #tabla['fecha'][0]=pd.to_datetime(str(tabla['fecha'][0])+" "+str(tabla['hora'][0]))

    for i in tabla['fecha']:
        tabla['fecha'][ix]=pd.to_datetime(str(i)+" "+str(tabla['hora'][ix]))
        ix=ix+1
        


    
    #print("tabla leida")
    
    fechaNula = pd.to_datetime('2023-01-01 00:00:00')
    def deltaOK(lista,i):
        return True
    Nmin = tabla['nivel'][0]
    w = 0
    for i in range(len(tabla)):
        #print(i,"Valor actual y valor minimo:", tabla['nivel'][i],Nmin)
        if tabla['nivel'][i] <= Nmin:
            #print("un menor   ",i,"Valor actual y valor minimo:", tabla['nivel'][i],Nmin)
            if deltaOK(tabla,i):
                Nmin = float(tabla['nivel'][i] )
                tabBot['fecha_min'][w]=tabla['fecha'][i]
                tabBot['fecha_fin'][w]=fechaNula
                tabBot['N_minimo'][w]=float(Nmin)
                tabBot['N_maximo'][w]=0.0
                tabBot['incremento'][w]=0.0
            else:
                pass
        else:
            if tabla['nivel'][i]-tabBot['N_minimo'][w] >= DN_botella:
                #print(w,tabla['nivel'][i]-tabBot['N_minimo'][w])
                fecha1 = tabBot['fecha_min'][w]
                fecha2 = tabla['fecha'][i]
                diferencia = fecha2 - fecha1
                #print("i=",i,"w=",w,"fecha2= ",fecha2, "fecha1= ", fecha1, "Delta= ", diferencia)
                if diferencia >= datetime.timedelta(minutes=TbotellaMin):
                    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    #print("        llego una botella")
                    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
                    Nmin = tabla['nivel'][i] 
                    #tabBot['fecha_min'][w]=
                    tabBot['fecha_fin'][w]=tabla['fecha'][i]
                    #tabBot['N_minimo'][w]=Nmin
                    tabBot['N_maximo'][w]=tabla['nivel'][i]
                    tabBot['incremento'][w]=tabBot['N_maximo'][w]-tabBot['N_minimo'][w]
                    tabBot = pd.concat([tabBot,filaNula],ignore_index=True)
                    
                    w  = len(tabBot)-1
                    tabBot['fecha_min'][w]=tabla['fecha'][i]
                    tabBot['fecha_fin'][w]=fechaNula
                    tabBot['N_minimo'][w]=Nmin
                    tabBot['N_maximo'][w]=0
                    tabBot['incremento'][w]=0 
                else:
                    pass
            else:
                pass
        

    #print(tabBot)
    return tabBot
########

dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(year, month, day), nombre_silo ='Silo 21-2').values()))
tablaBotellasSilo21_2 = tablaBotellas(dfSilo)
print("#####################################")
print("        Tabla de Botellas 21-2")
print("#####################################")
print("        ")
print(tablaBotellasSilo21_2)
dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(year_ayer, month_ayer, day_ayer), nombre_silo ='Silo 21-3').values()))
tablaBotellasSilo21_3 = tablaBotellas(dfSilo)
print("#####################################")
print("        Tabla de Botellas 21-3")
print("#####################################")
print("        ")
print(tablaBotellasSilo21_3)
dfSilo = pd.DataFrame(list(Valoressensores.objects.filter(fecha__gte=datetime.datetime(year, month, day), nombre_silo ='Silo 25-3').values()))
tablaBotellasSilo25_3 = tablaBotellas(dfSilo)
print("#####################################")
print("        Tabla de Botellas 25-3")
print("#####################################")
print("        ")
print(tablaBotellasSilo25_3)






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
