# -*- coding: utf-8 -*-
"""
Creado en Mayo 26 de 2022
Programa para hacer pedidos de cemento a ArgosOne en funcion del nivel de los silos
-. Guardar los pedidos en la tabla "components_pedidos" esta tabla contiene hasta 5 pedidos por silo y contiene todos los pedidos realizados por este sistema.
    La idea es que al generar un pedido se escribe en la base de datos components_pedidos y si llega una botella a ese silo se marca el pedido mas viejo como entregado
    la base de datos guarda los pedidos abiertos y cerrados historicos.
class pedidos(models.Model):
    pedidos_id          =   models.BigIntegerField(db_column='pedido_id', blank=True, null=True)
    codigo_sap          =   models.BigIntegerField(db_column='codigo_sap', blank=True, null=True)
    description         =   models.TextField(db_column='description', blank=True, null=True)
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)
    nivel_porcen        =   models.FloatField(db_column='nivel_porcen', blank=True, null=True)                     #Porcentaje de Nivel
    nivel_metros        =   models.FloatField(db_column='nivel_metros', blank=True, null=True)                    #Nivel en Metros
    estado_pedido       =   models.IntegerField(db_column='estado_pedido', blank=True, null=True)           # 1 pedido abierto y 2 pedido cerrado
    fecha_pedido        =   models.DateTimeField(db_column='fecha_pedido', blank=True, null=True)           #Fecha del Pedido
    fecha_cerrado       =   models.DateTimeField(db_column='fecha_cerrado', blank=True, null=True)         #Fecha del Pedido

class silos(models.Model):
    silo                =   models.TextField(db_column='silo', blank=True, null=True)
    material            =   models.TextField(db_column='material', blank=True, null=True)
    codigo_sap          =   models.BigIntegerField(db_column='codigo_sap', blank=True, null=True)
    description         =   models.TextField(db_column='description', blank=True, null=True)
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)
    nivel               =   models.FloatField(db_column='nivel', blank=True, null=True)
    metros              =   models.FloatField(db_column='metros', blank=True, null=True)
    estado_silo         =   models.TextField(db_column='estado_silo', blank=True, null=True)
    fecha_estado_silo   =   models.DateTimeField(db_column='fecha_estado_silo', blank=True, null=True)
    estado_pedido       =   models.TextField(db_column='estado_pedido', blank=True, null=True)
    fecha_estado_pedido =   models.DateTimeField(db_column='fecha_estado_pedido', blank=True, null=True)
    ultimo_llenado      =   models.DateTimeField(db_column='ultimo_llenado', blank=True, null=True)

Hola Jaime, cómo estás?
 
Con respecto a la información que habitualmente se requiere para la creación de un pedido, te detallo dicho requerimiento:
 
Código SAP de cliente
Código de producto
Cantidad de toneladas
Incoterm: entrega o retira
Fecha de entrega
Número del silo
 
Dentro del alcance del proyecto de granel por consumo, como iniciaremos con un piloto en Plantas de Concreto nuestras y Planta de Mortero, el correo debe ser enviado a 
Manuela Gonzalez (mgonzalezh@argos.com.co), con 
copia a:
Alda Eleane Pinzón (alda.pinzon@argos.co)
Victor Moreno (victor.moreno@argos.co).
 
Cuando se masifique a clientes, entonces el correo debería ser enviado al Contact Center (contactenos@argos.co), pero será en una fase más adelante.
 
Se me ocurre que con la finalidad de dar una atención prioritaria a estas solicitudes, en el asunto del correo pongamos algo como “PRIORITARIO: PEDIDO POR GENERACIÓN AUTOMÁTICA DE GRANEL”, distinguiéndolo así de los n-mil correos que se puedan recibir por día.
 
Saludos,
 
Mateo Londoño

@author: Alejandro Alvarado
class silos(models.Model):
    silo                =   models.CharField(db_column='silo', max_length=20, blank=True, null=True)
    planta              =   models.CharField(db_column='planta', max_length=80, blank=True, null=True)
    codigo_sap          =   models.ForeignKey(material, default= 1, on_delete=models.CASCADE,related_name='productos')
    toneladas           =   models.FloatField(db_column='toneladas', blank=True, null=True)
    nivel               =   models.FloatField(db_column='nivel', blank=True, null=True)
    metros              =   models.FloatField(db_column='metros', blank=True, null=True)
    estado_silo         =   models.TextField(db_column='estado_silo', blank=True, null=True)
    fecha_estado_silo   =   models.DateTimeField(db_column='fecha_estado_silo', blank=True, null=True)
    estado_pedido       =   models.TextField(db_column='estado_pedido', blank=True, null=True)
    fecha_estado_pedido =   models.DateTimeField(db_column='fecha_estado_pedido', blank=True, null=True)
    ultimo_llenado      =   models.DateTimeField(db_column='ultimo_llenado', blank=True, null=True)
    radio_cilindro      =   models.FloatField(db_column='radio_cilindro',blank=True, null=True) #(m) Para calcular el volumen del cilindro del SILO m^3 Volumen = Pi * r^2 * h
    altura_cilindro     =   models.FloatField(db_column='altura_cilindro',blank=True, null=True) #(m) Para calcular el volumen maximo del cilindro de SILO m^3
    setpoint            =   models.FloatField(db_column='setpoint',blank=True, null=True) # Valor en Metros desado para mantener el nivel.

"""
# Establece conexion con los modelos de las tablas de DJANGO.
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skote.settings")
django.setup()
from components.models import pedidos, silos, material

def realizarPedido(planta,siloA,pedido_id):
    #Concretos ARGOS Tocumen
    silo =silos.objects.filter(silo = siloA)
    #print(silo)
    # Creacion de fecha para el email
    import datetime
    from send_mailv2 import mail

    day     = datetime.date.today().day
    year    = datetime.date.today().year
    month   = datetime.date.today().month
    for i in silo:
        nombre_cemento = i.codigo_sap
        cantidad = 28
        unidad = 'ton'
        planta ='Planta de Concretos Tocumen'
        Codigo_SAP_de_cliente = 221
        Codigo_de_producto = i.codigo_sap
        Cantidad_de_toneladas = 28
        porcentaje = i.nivel
        toneladas = round(i.nivel*28*9/100,2)
        Incoterm_entrega ='Entrega'
        Fecha_de_entrega = f"{day}/{month}/{year}"
        Numero_del_silo = i.silo
    


    
    subject = f"PRIORITARIO: PEDIDO POR GENERACIÓN AUTOMÁTICA DE GRANEL {day}/{month}/{year}"
    l1 =f"PRIORITARIO: PEDIDO POR GENERACIÓN AUTOMÁTICA DE GRANEL {day}/{month}/{year}  Planta: {planta}\n"
    l2 =f"Número de Pedido          : {pedido_id}\n"
    l3 =f"Código SAP de cliente     : {Codigo_SAP_de_cliente}\n"
    l4 =f"Código de producto        : {Codigo_de_producto}\n"
    l5 =f"Cantidad de toneladas     : {Cantidad_de_toneladas}\n"
    l6 =f"Incoterm: entrega o retira: {Incoterm_entrega}\n"
    l7 =f"Fecha de entrega          : {Fecha_de_entrega}\n"
    l8 =f"Número del silo           : {Numero_del_silo}\n"
    l9 =f"Nivel Actual Silo (%)      : {porcentaje}\n"
    l10 =f"Nivel Actual Toneladas (ton) : {toneladas} ton \n"
    body = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10
    
    destinatarios = [
        "manuela.gonzalez@argos.co",
        "jose.chiru@argos.co",
        "ilenne.serrano@argos.co",
        "domingo.delrio@argos.co",
        "victor.lima@argos.co",
        "jcaicedo@argos.com.co",
        "mateo.londono@argos.co",
        "aljadis.sanchez@argos.co",
        "mario.cabrera@argos.co",
        "aalvarado@qptechllc.com"
    ]
    mail(destinatarios, subject, body)
    
    return True

#realizarPedido("Planta Tocumen","Silo 25-3",934)