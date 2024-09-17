# Establece conexion con los modelos de las tablas de DJANGO.
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skote.settings")
django.setup()

def calculopedido(planta,silo):
    from components.models import pedidos, silos, material
    import datetime
    import pytz
    from PedidosTocumen import realizarPedido

    # create a datetime object in some timezone, for example UTC
    dt = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

    # convert to Panama timezone
    panama_tz = pytz.timezone('America/Panama')
    panama_dt = dt.astimezone(panama_tz)
    setpoint = silo.setpoint  # 8 Metros punto de pedido

    # Conteo de Pedidos
    NumPedidos = (pedidos.objects.filter(planta = planta, nom_silo = silo.silo,id_tablaLlegadas = None, fecha_pedido__gte = "2023-01-01")).count()

    CalcNewPerdido = setpoint - NumPedidos * silo.metrosxbotella - silo.metros
    
    if CalcNewPerdido>=silo.metrosxbotella:
        pedlast = pedidos.objects.filter(planta = planta, nom_silo = silo.silo).last()
        ped = pedidos(n_maximo = pedlast.n_maximo, planta = planta,nom_silo =silo.silo, fecha_max = pedlast.fecha_max)
        ped.codigo_sap  = silo.codigo_sap.id
        ped.description = ''
        ped.toneladas   = silo.metros/silo.metrosxbotella*28 # 28 toneladas por botella
        ped.nivel_porcen= silo.metros/silo.altura_cilindro*100
        ped.nivel_metros= silo.metros
        ped.estado_pedido=1
        ped.fecha_pedido= panama_dt
        #ped.fecha_cerrado
        ped.ton_max     = silo.altura_cilindro/silo.metrosxbotella*28
        #n_maximo
        ped.decremento = ped.n_maximo - ped.nivel_metros
        #fecha_max
        #ped.id_tablaLlegadas = 0
        ped.id_sensorP      = pedlast.id_sensorP + 10   ##### ID DE LA TABLA DE VALOR DEL SENSOR QUE DISPARO EL PEDIDO (deberia venir de silo)
        if ped.nivel_porcen > 70:
            ped.prioridad = 3
        elif ped.nivel_porcen > 50:
            ped.prioridad = 2
        else:
            ped.prioridad = 1
        ped.save()
        silo.fecha_estado_pedido = panama_dt
        silo.estado_pedido = f"Hay {NumPedidos+1} pedidos para este silo"
        silo.save()
        realizarPedido("Planta Tocumen",silo.silo,ped.id)
        return True
    else:
        return False

#Concretos ARGOS Tocumen
#silo21_2=silos.objects.get(pk=1)
#silo21_3=silos.objects.get(pk=2)
#silo25_3=silos.objects.get(pk=3)

#print(calculopedido("Concretos Tocumen", silo21_2))
#print(calculopedido("Concretos Tocumen", silo21_3))
#print(calculopedido("Concretos Tocumen", silo25_3))

