import pandas as pd
import pyodbc
import psycopg2
import datetime

server1 = 'FTV-VIEWPOINT\ARGOSLABSQL' # base de datos de LABORATORIO
server2 = 'FTV-VIEWPOINT\SQLEXPRESS' #Reporte de Toneladas de Cemento
database1 = 'Laboratorio'
database2 = 'QPTECH'
username = 'qptech' 
password = '#Argos2017' 
connLAB = pyodbc.connect('DRIVER={SQL Server};SERVER='+server1+';DATABASE='+database1+';UID='+username+';PWD='+ password)    
connTON = pyodbc.connect('DRIVER={SQL Server};SERVER='+server2+';DATABASE='+database2+';UID='+username+';PWD='+ password)

query = "select * from CargarHorarios WHERE fecha > '2023-04-01'"

dfEncabezado = pd.read_sql(query,connLAB)

#for i in dfEncabezado:
idBajoEncabezado = int(dfEncabezado['CargarHorarioId'][0]) -1
query2 = f"select * from DatoHorarios where CargarHorarioId > {idBajoEncabezado}"

dfColumnas = pd.read_sql(query2,connLAB)
connLAB.close()
connTON.close()

nuevo_df = pd.merge(dfEncabezado, dfColumnas[['CargarHorarioId', 'DatoId']], on='CargarHorarioId', how='inner')
#dfEncabezado.merge(dfColumnas,how='left',on='CargarHorarioId')

#conteo1 = dfColumnas['CargarHorarioId'].value_counts()[9627]
#conteo2 = dfColumnas['CargarHorarioId'].value_counts()[9628]
#conteo3 = dfColumnas['CargarHorarioId'].value_counts()[9753]
#conteo4 = dfColumnas['CargarHorarioId'].value_counts()[9754]
nuevo_df.to_excel("ReporteHorario.xlsx",index=False)
print(nuevo_df)
"""
CargarHorarios
DatoHorarios

Tablas de Seleccion
DatoManual
Dato
ProductosSpec ?? No se que hace
Molinos
Productos (Cementos)
"""