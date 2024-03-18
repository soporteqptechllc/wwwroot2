# Programa en Python que se ejecutara por el Administrador de tareas,
# este programa lee unos datos/tablas para ser cargados en una tabla
# de la base de datos de postgreSQL

# Import Model
import os
import django
# Import pytz
import pytz
import datetime
# Import environment variables 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "argos_ml_project.settings.local")
django.setup()
# Import Model Datetime
from datetime import datetime
# Import Model Django
from applications.boquillas.models import boquillas,productos, mezclado
# Import Model pycomm3
from pycomm3 import LogixDriver, SLCDriver

# ****************************************************
# Funcion para guardar los datos en la Base de Datos 
# ****************************************************
tz = pytz.timezone('America/Bogota') # current time zone local


# ****************************************************    
# Lectura de dstos de PLC y escritura en base PostgreSQL
# **************************************************** 
# Leer la ultima fila de la tabla de mezclado
#mezclado_last = mezclado.objects.last()

# Valido si existe la fila y el dato del campo batch_id
# if mezclado_last:
#     batch_id_last = mezclado.batch_id
# else:
#     batch_id_last = 0
  
# print('batch_id      :', batch_id_last)

# Leer los datos de PLC y crear unas listas
with LogixDriver('192.168.0.11') as CompacTLogixML:
    PLC_ReporteMezclado = CompacTLogixML.read('ReporteMezclado{19}')
    Registros = PLC_ReporteMezclado[1]
print(Registros[0]['Batch_ID'])  
for x in Registros:   
    if not mezclado.objects.filter(batch_id=x['Batch_ID']).exists():
        dataf1 = x['Year_start']
        dataf2 = x['Month_start']
        dataf3 = x['Day_start']
        dataf4 = x['Hour_start']
        dataf5 = x['Minute_start']
        dataf6 = x['Second_start']
        datatxt = str(dataf2)+'/'+str(dataf3) +'/'+str(dataf1)+' '+ str(dataf4)+':'+str(dataf5)+':'+'00'
        dataf = datetime.strptime(datatxt,"%m/%d/%Y %H:%M:%S")
        datafz = tz.localize(dataf)
        #print(datafz)
        data_sp = 0.0
        data_sp = data_sp+round(x['BZ_Agre1_SP'],3)+round(x['BZ_Agre2_SP'],3)+round(x['BZ_Agre3_SP'],3)+round(x['BZ_Agre4_SP'],3)
        data_sp = data_sp+round(x['BZ_Cem1_SP'],3)+round(x['BZ_Cem2_SP'],3)+round(x['BZ_Adit_SP'],3)
        data_pv = 0.0
        data_pv = data_pv+round(x['BZ_Agre1_PV'],3)+round(x['BZ_Agre2_PV'],3)+round(x['BZ_Agre3_PV'],3)+round(x['BZ_Agre4_PV'],3)
        data_pv = data_pv+round(x['BZ_Cem1_PV'],3)+round(x['BZ_Cem2_PV'],3)+round(x['BZ_Adit_PV'],3)
        data_ton = round(data_pv/1000,3)
        id_prod = productos.objects.filter(id_Producto = 4626415).first() # Falta por cargar el ID del Producto
        des_prod = id_prod.name     
        print('New Batch_ID')
        new_registro = mezclado() # Indexación a la tabla Mezclado
        new_registro.batch_id = x['Batch_ID']
        new_registro.lote = x['Lote']
        new_registro.id_producto   = id_prod
        new_registro.name_producto = des_prod
        new_registro.silo1= round(x['Silo1'],3)
        new_registro.silo2 = round(x['Silo2'],3)
        new_registro.silo3 = round(x['Silo3'],3)
        new_registro.silo4 = round(x['Silo4'],3)
        new_registro.silo5 = round(x['Silo5'],3)
        new_registro.silo6 = round(x['Silo6'],3) 
        new_registro.silo7 = round(x['Silo7'],3)
        new_registro.silo8 = round(x['Silo8'],3)
        new_registro.year_start = x['Year_start']
        new_registro.month_start = x['Month_start']
        new_registro.day_start = x['Day_start']
        new_registro.hour_start = x['Hour_start']
        new_registro.minute_start = x['Minute_start']
        new_registro.socond_start = x['Second_start']
        new_registro.year_end = x['Year_end']
        new_registro.month_end = x['Month_end'] 
        new_registro.day_end = x['Day_end'] 
        new_registro.hour_end = x['Hour_end']
        new_registro.minute_end = x['Minute_end']
        new_registro.secound_end = x['Secound_end']
        new_registro.bz_agre1_sp = round(x['BZ_Agre1_SP'],3)
        new_registro.bz_agre1_pv = round(x['BZ_Agre1_PV'],3)
        new_registro.bz_agre2_sp = round(x['BZ_Agre2_SP'],3)
        new_registro.bz_agre2_pv = round(x['BZ_Agre2_PV'],3)
        new_registro.bz_agre3_sp = round(x['BZ_Agre3_SP'],3)
        new_registro.bz_agre3_pv = round(x['BZ_Agre3_PV'],3)
        new_registro.bz_agre4_sp = round(x['BZ_Agre4_SP'],3)
        new_registro.bz_agre4_pv = round(x['BZ_Agre4_PV'],3)
        new_registro.bz_cem1_sp = round(x['BZ_Cem1_SP'],3)
        new_registro.bz_cem1_pv = round(x['BZ_Cem1_PV'],3)
        new_registro.bz_cem2_sp = round(x['BZ_Cem2_SP'],3)
        new_registro.bz_cem2_pv = round(x['BZ_Cem2_PV'],3)
        new_registro.bz_adit_sp = round(x['BZ_Adit_SP'],3) 
        new_registro.bz_adit_pv = round(x['BZ_Adit_PV'],3)
        new_registro.time_mezcla = round(x['Time_Mezcla'],3)
        new_registro.total_sp = data_sp
        new_registro.total_pv = data_pv
        new_registro.total_ton = data_ton
        new_registro.datetime_plc = datafz
        new_registro.save()

# ****************************************************    
# FIN
 # ****************************************************   
