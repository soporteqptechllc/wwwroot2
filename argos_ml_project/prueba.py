
# Import datetime  
from datetime import date, datetime, timedelta
import os
import django
# Import environment variables 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "argos_ml_project.settings.local")
django.setup()
from applications.boquillas.models import boquillas
# Import requests 
#import requests
from applications.boquillas.send_mail import mail
from django.db.models import Count,Sum

year = date.today().year # current year
month = date.today().month # current month
day = date.today().day # current day
fecha0 = list()
fecha0 = ['01','01','2024']
fecha0[0] = day
fecha0[1] = month
fecha0[2] = year
file_name = str(f"Informe_Q&PTECH_Panama_{fecha0[0]}-{fecha0[1]}-{fecha0[2]}.xlsx")
file_path = str(f"C:/inetpub/wwwroot/argos_ml_project/excel/Informe_Q&PTECH_Panama_{fecha0[0]}-{fecha0[1]}-{fecha0[2]}.xlsx")

mail("jgarcia@qptechllc.com", "Buenos días, este es un email de envio automático de Q&P Tech Panamá Inc. - Informe de Proceso", file_name, file_path)

""" boquillasx = boquillas.objects.last()
#print(boquillasx)
result1 = boquillas.objects.values('name_producto').order_by('name_producto').annotate(count=Count('name_producto'))
result2 = boquillas.objects.values('name_producto').order_by('name_producto').annotate(total_peso=Sum('peso'))
result3 = boquillas.objects.values('name_producto').order_by('name_producto').annotate(total_peso=Sum('peso')).filter(n_boquilla = 1)
#print(result1)
#for i in result1:
#    print(i['name_producto'],i['count'])
for i in result2:
    print(i['name_producto'],i['total_peso'])
print('')
for i in result3:
    print(i['name_producto'],i['total_peso']) """

""" from pycomm3 import LogixDriver, SLCDriver

with LogixDriver('192.168.0.11') as CompacTLogixML:
    boquilla1 = CompacTLogixML.read('RegistroBQ1{20}')
    boquilla2 = CompacTLogixML.read('RegistroBQ2{20}')
    boquilla3 = CompacTLogixML.read('RegsitroBQ3{20}')

for registro in boquilla1[1]:
    print(registro) """

""" fechatxt = '7/14/2022 11:22:10 UTC'
dato = datetime.strptime(fechatxt,"%m/%d/%Y %H:%M:%S %Z")
print("date:", dato) """

""" from datetime import datetime, timedelta

navidad = datetime.strptime("2021-12-25", "%Y-%m-%d")
fin_anio = datetime.strptime("2021-12-31", "%Y-%m-%d")
diferencia = fin_anio-navidad
print(f"La diferencia es de {diferencia.days} días y {diferencia.seconds} segundos. La diferencia total es de {diferencia.total_seconds()} segundos") """

""" from itertools import groupby

numeros = [1,1,2,2,3,3]
print(numeros)
grupos_numeros = groupby(numeros)
for k,g in grupos_numeros:
    print(k)
    print(list(g)) """