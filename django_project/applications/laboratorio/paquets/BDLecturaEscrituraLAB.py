# -*- coding: utf-8 -*-
# Consulta Basica de una Base de Datos ya creada en SQLServer,
# leer la Base de Datos "Lavoratorio" y luego escribir los
# Datos procesado en una Base de Datos ya creada en PostgreSQL

from zmq import NULL
from ..models import ReporteLAB
# Import SQLServer
import pyodbc
# Import PostgreSQL
import psycopg2
import datetime
colufecha = list()
colu0 = list()
colu1 = list()
colu2 = list()
colu3 = list()
colu4 = list()
colu5 = list()
colu6 = list()
colu7 = list()
colu8 = list()
colu9 = list()
colu10 = list()
colu11 = list()
colu12 = list()
coluK = list()
coluL = list()
coluM = list()
coluN = list()
coluO = list()
coluP = list()
coluQ = list()
coluR = list()
coluS = list()
coluT = list()
coluU = list()
coluW = list()
coluX = list()
coluY = list()
coluZ = list()
coluAA = list()
coluAB = list()
coluAC = list()
coluAD = list()
coluAE = list()
coluAF = list()
coluAG = list()
coluAH = list()
coluAI = list()
coluAJ = list()
coluAK = list()
coluAL = list()
coluAM = list()
coluAN = list()
coluAS = list()
coluAT = list()
coluAU = list()
coluAV = list()
coluAW = list()
coluAX = list()
coluAY = list()
coluAZ = list()
coluBA = list()
coluBB = list()
coluBC = list()
coluBD = list()
coluBE = list()
coluBF = list()
coluBG = list()
coluBH = list()
coluBI = list()
coluBJ = list()
coluBK = list()
coluBL = list()
coluBM = list()
coluCB = list()
coluCC = list()

fecha = list()
fecha = ['01','01','2021']
day = datetime.date.today().day
year    = datetime.date.today().year
month   = datetime.date.today().month
fecha[0] = day
fecha[1] = month
fecha[2] = year
# Conexion a tu base de datos

# Usa el método conectar()
try:
    server1 = 'FTV-VIEWPOINT\ARGOSLABSQL' 
    server2 = 'FTV-VIEWPOINT\SQLEXPRESS'
    database1 = 'Laboratorio'
    database2 = 'QPTECH'
    username = 'qptech' 
    password = '#Argos2017' 
    cnxn1 = pyodbc.connect('DRIVER={SQL Server};SERVER='+server1+';DATABASE='+database1+';UID='+username+';PWD='+ password)    
    cnxn2 = pyodbc.connect('DRIVER={SQL Server};SERVER='+server2+';DATABASE='+database2+';UID='+username+';PWD='+ password)
    #cnxn3 = psycopg2.connect("dbname=laboratorio_db user=qptech password=#Argos2017")
    
    cursor1 = cnxn1.cursor()
    cursor2 = cnxn2.cursor()
    credenciales = {
        "dbname": "laboratorio_db",
        "user": "qptech",
        "password": "#Argos2017",
        "host": "localhost",
        "port": ''
    }
    cnxn3 = psycopg2.connect(**credenciales)   
    cursor3 = cnxn3.cursor()
    # ****************************** INICIO DESPACHO **********************************************
    # Declaro variable de id de cemento
    print("Inicio de la creacion de las filas 0 al 12")
    # Crear el texto del Query
    texto_query = """
    SELECT 
    Cemento,
    ProductoId,
    CargarPromedioId,
    C_Fecha,
    MONTH(C_Fecha),
    DATEPART(week,C_Fecha),
    G_Molino,
    H_Destino,
    V_FAnalista,
    BL_QAnalista,
    CC_Comentarios
    FROM Excel2_L_V 
    WHERE ProductoId in (1,2,3,4,7,8,9,10,11,12,14,29,31,32)
    ORDER BY ProductoId,C_Fecha
    """
    # Ejecutar una consulta
    cursor1.execute(texto_query)
    # Se crean las primeras listas que van en la hoja de Excel   
    while 1:
        row = cursor1.fetchone()
        if not row:
            break
        colu0.append(row[0])
        colu1.append(row[1])
        colu2.append(row[2])
        colufecha.append(row[3])
        colu3.append(datetime.datetime.strptime(row[3],"%Y-%m-%d"))
        if row[4] == 1:
            colu4.append('ENERO')
        elif row[4] == 2:
            colu4.append('FEBRERO')
        elif row[4] == 3:
            colu4.append('MARZO')
        elif row[4] == 4:
            colu4.append('ABRIL')
        elif row[4] == 5:
            colu4.append('MAYOR')
        elif row[4] == 6:
            colu4.append('JUNIO')
        elif row[4] == 7:
            colu4.append('JULIO')
        elif row[4] == 8:
            colu4.append('AGOSTO')
        elif row[4] == 9:
            colu4.append('SEPTIEMBRE')
        elif row[4] == 10:
            colu4.append('OCTUBRE')
        elif row[4] == 11:
            colu4.append('NOVIEMBRE')
        elif row[4] == 12:
            colu4.append('DICIEMBRE')
        colu5.append(row[5])
        colu6.append(row[6])
        colu7.append(row[7])   
        colu8.append(row[8])
        colu9.append(row[9])
        colu10.append(row[10])
        colu11.append('Local - Cartagena')
        if row[1] in (8,9,10,11,12,14,29,32):
            colu12.append('DESP')
        elif row[1] in (1,2,3,4,7,31):
            colu12.append('PROD')
        #print(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])

    # Se crean las listas de las Columna que van en la hoja de Excel
    for i in colu3:
        coluK.append('')
        coluL.append('')
        coluM.append('')
        coluN.append('')
        coluO.append('')
        coluP.append('')
        coluQ.append('')
        coluR.append('')
        coluS.append('')
        coluT.append('')
        coluU.append('')
        coluW.append('')
        coluX.append('')
        coluY.append('')
        coluZ.append('')
        coluAA.append('')
        coluAB.append('')
        coluAC.append('')
        coluAD.append('')
        coluAE.append('')
        coluAF.append('')
        coluAG.append('')
        coluAH.append('')
        coluAI.append('')
        coluAJ.append('')
        coluAK.append('')
        coluAL.append('')
        coluAM.append('')
        coluAN.append('')
        coluAS.append('')
        coluAT.append('')
        coluAU.append('')
        coluAV.append('')
        coluAW.append('')
        coluAX.append('')
        coluAY.append('')
        coluAZ.append('')
        coluBA.append('')
        coluBB.append('')
        coluBC.append('')
        coluBD.append('')
        coluBE.append('')
        coluBG.append('')
        coluBH.append('')
        coluBI.append('')
        coluBJ.append('')
        coluBK.append('')
        coluBM.append(0.0)
    print("Inicio de la creacion de las filas K a BM")
        # Se Buscan los datos de las demas Columnas
    for cid in colu2:
        #print(cid)
        # Crear el texto del Query
        texto_query = """SELECT DatoId,CargarPromedioId,Valor,Tipo
                        FROM DatoPromedios
                        WHERE CargarPromedioId = %s
                        ORDER BY DatoId""" % (cid)
        # Ejecutar una consulta
        cursor1.execute(texto_query)
        while 1:
            row = cursor1.fetchone()
            fila = colu2.index(cid)

            if not row:
                break
            #print(row[0])
            if row[3] == 0 and row[0] ==  70:               
                if not row[2]:
                    coluK[fila] = row[2]
                else:
                    coluK[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  71:
                if not row[2]:
                    coluL[fila] = row[2]
                else:
                    coluL[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  72:
                if not row[2]:
                    coluM[fila] = row[2]
                else:
                    coluM[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  73:
                if not row[2]:
                    coluN[fila] = row[2]
                else:
                    coluN[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  74:
                if not row[2]:
                    coluO[fila] = row[2]
                else:
                    coluO[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  69:               
                if not row[2]:
                    coluP[fila] = row[2]
                else:
                    coluP[fila] = float(row[2])/100
            elif row[3] == 1 and row[0] ==  31: # Tipo 1 columna P              
                if not row[2]:
                    coluP[fila] = row[2]
                else:
                    coluP[fila] = float(row[2])/100                    
            elif row[3] == 0 and row[0] ==  48:
                if not row[2]:
                    coluQ[fila] = row[2]
                else:
                    coluQ[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  68:
                if not row[2]:
                    coluR[fila] = row[2]
                else:
                    coluR[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  44:
                if not row[2]:
                    coluS[fila] = row[2]
                else:
                    coluS[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  42: # OJO (:)               
                if not row[2]:
                    coluT[fila] = row[2]
                elif ':' in row[2]:
                    if int(row[2][row[2].find(':')+1:]) > 49:
                        coluT[fila] = int(row[2][0:row[2].find(':')]) + 1
                    else:
                        coluT[fila] = int(row[2][0:row[2].find(':')])
                else:
                    coluT[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  43:  # OJO (:)
                if not row[2]:
                    coluU[fila] = row[2]
                elif ':' in row[2]:
                    if int(row[2][row[2].find(':')+1:]) > 49:
                        coluU[fila] = int(row[2][0:row[2].find(':')]) + 1
                    else:
                        coluU[fila] = int(row[2][0:row[2].find(':')])
                else:
                    coluU[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  45:
                if not row[2]:
                    coluW[fila] = row[2]
                else:
                    coluW[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  67:
                if not row[2]:
                    coluX[fila] = row[2]
                else:
                   coluX[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  54:
                if not row[2]:
                    coluY[fila] = row[2]
                else:
                    coluY[fila] = float(row[2])                                                                     
            elif row[3] == 0 and row[0] ==  55:
                if not row[2]:
                    coluZ[fila] = row[2]
                else:
                    coluZ[fila] = float(row[2])                    
            elif row[3] == 0 and row[0] ==  56:
                if not row[2]:
                    coluAA[fila] = row[2]
                else:
                    coluAA[fila] = float(row[2])                    
            elif row[3] == 0 and row[0] ==  57:
                if not row[2]:
                    coluAC[fila] = row[2]
                else:
                    coluAC[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  58:
                if not row[2]:
                    coluAD[fila] = row[2]
                else:
                    coluAD[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  59:
                if not row[2]:
                    coluAE[fila] = row[2]
                else:
                    coluAE[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  60:
                if not row[2]:
                    coluAG[fila] = row[2]
                else:
                    coluAG[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  61:
                if not row[2]:
                    coluAH[fila] = row[2]
                else:
                    coluAH[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  62:
                if not row[2]:
                    coluAI[fila] = row[2]
                else:
                    coluAI[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  63:
                if not row[2]:
                    coluAK[fila] = row[2]
                else:
                    coluAK[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  64:
                if not row[2]:
                    coluAL[fila] = row[2]
                else:
                    coluAL[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  65:
                if not row[2]:
                    coluAM[fila] = row[2]
                else:
                    coluAM[fila] = float(row[2])
            elif row[3] == 0 and row[0] ==  66:
                if not row[2]:
                    coluAS[fila] = row[2]
                else:
                    coluAS[fila] = float(row[2])
            elif row[3] == 1 and row[0] ==  28: # Tipo de dato 1 columna AS
                if not row[2]:
                    coluAS[fila] = row[2]
                else:
                    coluAS[fila] = float(row[2])                    
            elif row[3] == 0 and row[0] ==  3:
                if not row[2]:
                    coluAT[fila] = row[2]
                else:
                    coluAT[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  6:
                if not row[2]:
                    coluAU[fila] = row[2]
                else:
                    coluAU[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  7:
                if not row[2]:
                    coluAV[fila] = row[2]
                else:
                    coluAV[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  8:
                if not row[2]:
                    coluAW[fila] = row[2]
                else:
                    coluAW[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  9:
                if not row[2]:
                    coluAX[fila] = row[2]
                else:
                    coluAX[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  10:
                if not row[2]:
                    coluAY[fila] = row[2]
                else:
                    coluAY[fila] = float(row[2])/100 
            elif row[3] == 0 and row[0] ==  11:
                if not row[2]:
                    coluAZ[fila] = row[2]
                else:
                    coluAZ[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  12:
                if not row[2]:
                    coluBA[fila] = row[2]
                else:
                    coluBA[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  13:
                if not row[2]:
                    coluBB[fila] = row[2]
                else:
                    coluBB[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  14:
                if not row[2]:
                    coluBC[fila] = row[2]
                else:
                    coluBC[fila] = float(row[2])/100
            elif row[3] == 1 and row[0] ==  26: # Tipo de dato 1 Columna BD
                if not row[2]:
                    coluBD[fila] = row[2]
                else:
                    coluBD[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  52:
                if not row[2]:
                    coluBE[fila] = row[2]
                else:
                    coluBE[fila] = float(row[2])/100
            elif row[3] == 1 and row[0] ==  27: # Tipo de dato 1 Columna BG
                if not row[2]:
                    coluBG[fila] = row[2]
                else:
                    coluBG[fila] = float(row[2])/100                    
            elif row[3] == 0 and row[0] ==  30:
                if not row[2]:
                    coluBH[fila] = row[2]
                else:
                    coluBH[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  31:
                if not row[2]:
                    coluBI[fila] = row[2]
                else:
                    coluBI[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  32:
                if not row[2]:
                    coluBJ[fila] = row[2]
                else:
                    coluBJ[fila] = float(row[2])/100
            elif row[3] == 0 and row[0] ==  33:
                if not row[2]:
                    coluBK[fila] = row[2]
                else:
                    coluBK[fila] = float(row[2])/100
        # **********************************************************************************
        # **********************************************************************************             
        # Columnas con calculo AB
        if not coluY[fila] and not coluZ[fila] and not coluAA[fila]:
            coluAB[fila] = 0.0            
        elif coluY[fila] and not coluZ[fila] and not coluAA[fila]:
            coluAB[fila] = coluY[fila]
        elif not coluY[fila] and coluZ[fila] and not coluAA[fila]:
            coluAB[fila] = coluZ[fila]
        elif coluY[fila] and coluZ[fila] and not coluAA[fila]:
            coluAB[fila] = float(coluY[fila] + coluZ[fila])/2
        elif not coluY[fila] and not coluZ[fila] and coluAA[fila]:
            coluAB[fila] = coluAA[fila]
        elif coluY[fila] and not coluZ[fila] and coluAA[fila]:
            coluAB[fila] = float(coluY[fila] + coluAA[fila])/2 
        elif not coluY[fila] and coluZ[fila] and coluAA[fila]:
            coluAB[fila] = float(coluZ[fila] + coluAA[fila])/2
        elif coluY[fila] and coluZ[fila] and coluAA[fila]:
            coluAB[fila] = float(coluY[fila] + coluZ[fila] + coluAA[fila])/3
        # Columnas con calculo AF
        if not coluAC[fila] and not coluAD[fila] and not coluAE[fila]:
            coluAF[fila] = 0.0            
        elif coluAC[fila] and not coluAD[fila] and not coluAE[fila]:
            coluAF[fila] = coluAC[fila]
        elif not coluAC[fila] and coluAD[fila] and not coluAE[fila]:
            coluAF[fila] = coluAD[fila]
        elif coluAC[fila] and coluAD[fila] and not coluAE[fila]:
            coluAF[fila] = float(coluAC[fila] + coluAD[fila])/2
        elif not coluAC[fila] and not coluAD[fila] and coluAE[fila]:
            coluAF[fila] = coluAE[fila]
        elif coluAC[fila] and not coluAD[fila] and coluAE[fila]:
            coluAF[fila] = float(coluAC[fila] + coluAE[fila])/2 
        elif not coluAC[fila] and coluAD[fila] and coluAE[fila]:
            coluAF[fila] = float(coluAD[fila] + coluAE[fila])/2
        elif coluAC[fila] and coluAD[fila] and coluAE[fila]:
            coluAF[fila] = float(coluAC[fila] + coluAD[fila] + coluAE[fila])/3
        # Columnas con calculo AJ
        if not coluAG[fila] and not coluAH[fila] and not coluAI[fila]:
            coluAJ[fila] = 0.0            
        elif coluAG[fila] and not coluAH[fila] and not coluAI[fila]:
            coluAJ[fila] = coluAG[fila]
        elif not coluAG[fila] and coluAH[fila] and not coluAI[fila]:
            coluAJ[fila] = coluAH[fila]
        elif coluAG[fila] and coluAH[fila] and not coluAI[fila]:
            coluAJ[fila] = float(coluAG[fila] + coluAH[fila])/2
        elif not coluAG[fila] and not coluAH[fila] and coluAI[fila]:
            coluAJ[fila] = coluAI[fila]
        elif coluAG[fila] and not coluAH[fila] and coluAI[fila]:
            coluAJ[fila] = float(coluAG[fila] + coluAI[fila])/2 
        elif not coluAG[fila] and coluAH[fila] and coluAI[fila]:
            coluAJ[fila] = float(coluAH[fila] + coluAI[fila])/2
        elif coluAG[fila] and coluAH[fila] and coluAI[fila]:
            coluAJ[fila] = float(coluAG[fila] + coluAH[fila] + coluAI[fila])/3
        # Columnas con calculo AN
        if not coluAK[fila] and not coluAL[fila] and not coluAM[fila]:
            coluAN[fila] = 0.0            
        elif coluAK[fila] and not coluAL[fila] and not coluAM[fila]:
            coluAN[fila] = coluAK[fila]
        elif not coluAK[fila] and coluAL[fila] and not coluAM[fila]:
            coluAN[fila] = coluAL[fila]
        elif coluAK[fila] and coluAL[fila] and not coluAM[fila]:
            coluAN[fila] = float(coluAK[fila] + coluAL[fila])/2
        elif not coluAK[fila] and not coluAL[fila] and coluAM[fila]:
            coluAN[fila] = coluAM[fila]
        elif coluAK[fila] and not coluAL[fila] and coluAM[fila]:
            coluAN[fila] = float(coluAK[fila] + coluAM[fila])/2 
        elif not coluAK[fila] and coluAL[fila] and coluAM[fila]:
            coluAN[fila] = float(coluAL[fila] + coluAM[fila])/2
        elif coluAK[fila] and coluAL[fila] and coluAM[fila]:
            coluAN[fila] = float(coluAK[fila] + coluAL[fila] + coluAM[fila])/3 
    print("Fin de la creacion de las listas")
    # **********************************************************************************      
    # **********************************************************************************
    print("Inicio del calculo de toneladas")
    #print(colufecha)
    # Declaro variable de id de cemento
    txtcemento = 'Concretero 42.5 KG'  # OJO Tambien esta el "Concretero 42.50 KG"
    # Crear el texto del Query
    texto_query = """SELECT FECHA, SUM(VALOR) 
    FROM Excel2_E_V 
    WHERE PRODUCTO LIKE \'Concretero 42.5%%\' AND COMPONENTE LIKE \'Despacho%%\'
    GROUP BY FECHA
    ORDER BY FECHA"""

    # Ejecutar una consulta
    cursor2.execute(texto_query)
 
    ctesuma = 0
    for f,v in cursor2:
        #print(f)        
        if f in colufecha:
            print(f)
            print(float(v)+float(ctesuma))
            #coluBM[colufecha.index(f)] = (float(v)+float(ctesuma))
            ctesuma = 0
        else:
            ctesuma += v      
    # **********************************************************************************
    # **********************************************************************************
    #print(coluBM)   
    # Query para borrar contenido de tabla
    # Ejecutar una Query
    cursor3.execute("TRUNCATE TABLE public.laboratorio_reportelab RESTART IDENTITY CASCADE")
    cnxn3.commit() # Confirmacion del Qury
    # Crear una lista con todas las lista de las columnas separadas
    listaG = zip(colu0,colu1,colu2,colu3,colu4,colu5,colu6,colu7,colu8,colu9,colu10,colu11,colu12,
                 coluK,coluL,coluM,coluN,coluO,coluP,coluQ,coluR,coluS,coluT,coluU,coluW,
                 coluX,coluY,coluZ,coluAA,coluAB,coluAC,coluAD,coluAE,coluAF,coluAG,coluAH,
                 coluAI,coluAJ,coluAK,coluAL,coluAM,coluAN,coluAS,coluAT,coluAU,coluAV,
                 coluAW,coluAX,coluAY,coluAZ,coluBA,coluBB,coluBC,coluBD,
                 coluBE,coluBG,coluBH,coluBI,coluBJ,coluBK,coluBM)
    # Query para insertar filas de la lista General en la tabla de PosgreSQL
    # Crear el texto del Query
    texto_query = """
    INSERT INTO laboratorio_reportelab(
    "cemento", 
    "productoid", 
    "cargarpromedioid", 
    datetime, 
    month, 
    week, 
    "molino", 
    "silo", 
    "fanalista", 
    "qanalista", 
    "comentarios",
    "proc_clinker",
    "tipo",
    "blaine_cm2g", 
    "retenido325",    
    "_330μm",
    "autoclave",
    "barras14dias",
    "contenidoaire",
    "retencionagua",
    "falsofraguado",
    "consistencianormal",
    "fraguadoi",
    "fraguadof",
    "aguacemento",
    "flujo",
    "r1cubo1",
    "r1cubo2",
    "r1cubo3",
    r1,
    "r3cubo1",
    "r3cubo2",
    "r3cubo3",
    r3,
    "r7cubo1",
    "r7cubo2",
    "r7cubo3",
    r7,
    "r28cubo1",
    "r28cubo2",
    "r28cubo3",
    r28,
    "densidad",
    "sio2",
    "ai2o3",
    "fe2o3",
    "cao",
    "mgo",
    "so3",
    "na2o",
    "k2o",
    "tio2",
    "p2o5",
    "pi",
    "callibre",
    ri,
    "c3s",
    "c2s",
    "c3a",
    "c4af",
    "toneladas"
    )
    VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
    %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"""    
    # Ejecutar una Query
    cursor3.executemany(texto_query, listaG)
    cnxn3.commit() # Confirmacion del Qury
# ****************************** FIN **********************************************

except Exception as e:
    print("Error de conexión SQLServer: ", e)
finally:
    # Se cierra la conexion SQL y la conexion al Servidos
    cursor1.close()  
    cnxn1.close()
    cursor2.close()  
    cnxn2.close()
    cursor3.close()  
    cnxn3.close()  
    #print("La conexión SQLServer está cerrada")