
import os, django
#Conexion con la base de datos de DJANGO
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skote.settings")
django.setup()
from components.models import pedidos, llegadas


def emparejar(planta,nom_silo):
    p = pedidos.objects.filter(planta = planta, nom_silo = nom_silo)
    for i in p:
        i.id_tablaLlegadas = None
        i.save()

    lle = llegadas.objects.filter(planta = planta, nom_silo = nom_silo, fecha_fin__gte = "2023-01-01").order_by('id_sensorLL')

    for j in lle:
        p3 = pedidos.objects.filter(planta = planta, nom_silo = nom_silo,id_tablaLlegadas = None, fecha_pedido__gte = "2023-01-01").order_by('id_sensorP')
        for i in p3:
            #print(i.id, i.id_tablaLlegadas)
            if j.id_sensorLL > i.id_sensorP:
                i.id_tablaLlegadas = j.id
                i.save()
                #print(j.id, i.id, i.id_tablaLlegadas)
                break
    return True


