#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
# C:\QPTECH\aalvarado\django_sap\VisualizacionReporteCremas.py
#from django.db import models
import os
import django
import datetime
import pandas as pd
# project_name nombre del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
django.setup()
from applications.api.models import operaciones, em_sp, RecetasSAP

# ****************************************************
# ****************************************************     
# funcion para listar operaciones de prod. en una tabla
def ListarDataTabla(idlote, idsem, idtipo):        
        # ********************************************    
        # Inicio de la creacion de las lista que van
        # en el cuerpo de la tabla
        # *********************************************               
        col1 = list()
        col2 = list()
        col3 = list()
        col4 = list()

        ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em10','em11','em15','em14','em16','humedad','ph']
        k = 0
        totem1 = totem2 = totem3 = totem4 = totem5 = totem6 = totem7 = totem8 = totem9 = totem10 = totem11 = 0.0
        totem15 = totem14 = tothum = totph = totrep = 0.0
        lista1 = em_sp.objects.filter(em__gt = 0).order_by("id")
        if idtipo == 1:
            lista2 = operaciones.objects.filter(idlote=idlote).exclude(idfabricacion = None).order_by("id")
        else:
            lista2 = operaciones.objects.filter(idfabricacion = None,idlote=idlote).order_by("id")
        lista3 = RecetasSAP.objects.filter(id_semielaborado = idsem).order_by('id_ingrediente')
        nolista1 = len(lista1)
        nolista2 = len(lista2)
        nolista3 = len(lista3)
        #print(nolista1)
        #print(nolista2)
        #print(nolista3)
        #print(lista1)
        #print(lista2)
        #print(lista3)
        x = 0
        y = 0

        for i in lista1:
            #print(i.ID)
            rec = RecetasSAP.objects.filter(id_semielaborado = idsem, id_ingrediente = i.ID).first()
            #print(rec)
            if x == 14:
                col1.append('')
                col2.append("TOTALES")
                col3.append("SUMATORIA")
                col4.append(0.0)
                col1.append(y)
                col2.append(i.ID)
                col3.append(i.Ingrediente)
                col4.append(i.SP)
                y += 1
            else:
                if rec and x < 14:
                    col1.append(y)
                    col2.append(i.ID)
                    col3.append(i.Ingrediente)
                    col4.append(i.SP)
                    y += 1
                elif x > 14:
                    col1.append(y)
                    col2.append(i.ID)
                    col3.append(i.Ingrediente)
                    col4.append(i.SP)
                    y += 1
                elif i.ID == 'AGUA':
                    col1.append(y)
                    col2.append(i.ID)
                    col3.append(i.Ingrediente)
                    col4.append(i.SP)
                    y += 1 
                elif i.ID == 'SE-REPROCESO':
                    col1.append(y)
                    col2.append(i.ID)
                    col3.append(i.Ingrediente)
                    col4.append(i.SP)
                    y += 1                                                  
            x += 1
        #print(col1,col2,col3,col4)
        if lista2:
                x = 1
                y = 0
                z = 0
                total = 0.0
                totaly = 0.0
                totalz = 0.0
                
                colt = list()

                for i in lista2:
                    
                    totem1 += i.em1
                    totem2 += i.em2
                    totem3 += i.em3
                    totem4 += i.em4
                    totem5 += i.em5
                    totem6 += i.em6
                    totem7 += i.em7
                    totem8 += i.em8
                    totem9 += i.em9
                    totem10 += i.em10
                    totem11 += i.em11
                    totem14 += i.em14
                    totem15 += i.em15
                    if i.humedad and i.humedad > 0:
                        tothum += i.humedad
                        y += 1
                    if i.ph and i.ph > 0:
                        totph += i.ph
                        z += 1
                    if i.reproceso and i.reproceso > 0:
                        totrep += i.reproceso

                    if x == 1:
                        col5 = list()
                        if 'MPDC00008' in col2:
                            col5.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col5.append(round(i.em2,1))
                            col5.append(round(i.em3,1))
                            col5.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col5.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col5.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col5.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col5.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col5.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col5.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col5.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col5.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col5.append(round(i.em14,1))
                        if i.reproceso:
                            col5.append(round(i.reproceso,1))
                        else:
                            col5.append(0.0)
                        col5.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col5.append(round(i.humedad,1))
                        else:
                            col5.append(0.0)
                        if i.ph:
                            col5.append(round(i.ph,1))
                        else:
                            col5.append(0.0)
                    if x == 2:
                        col6 = list()
                        if 'MPDC00008' in col2:
                            col6.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col6.append(round(i.em2,1))
                            col6.append(round(i.em3,1))
                            col6.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col6.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col6.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col6.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col6.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col6.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col6.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col6.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col6.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col6.append(round(i.em14,1))
                        if i.reproceso:
                            col6.append(round(i.reproceso,1))
                        else:
                            col6.append(0.0)
                        col6.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col6.append(round(i.humedad,1))
                        else:
                            col6.append(0.0)
                        if i.ph:
                            col6.append(round(i.ph,1))
                        else:
                            col6.append(0.0)
                    if x == 3:
                        col7 = list()
                        if 'MPDC00008' in col2:
                            col7.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col7.append(round(i.em2,1))
                            col7.append(round(i.em3,1))
                            col7.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col7.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col7.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col7.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col7.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col7.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col7.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col7.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col7.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col7.append(round(i.em14,1))
                        if i.reproceso:
                            col7.append(round(i.reproceso,1))
                        else:
                            col7.append(0.0)
                        col7.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col7.append(round(i.humedad,1))
                        else:
                            col7.append(0.0)
                        if i.ph:
                            col7.append(round(i.ph,1))
                        else:
                            col7.append(0.0)
                    if x == 4:
                        col8 = list()
                        if 'MPDC00008' in col2:
                            col8.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col8.append(round(i.em2,1))
                            col8.append(round(i.em3,1))
                            col8.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col8.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col8.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col8.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col8.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col8.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col8.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col8.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col8.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col8.append(round(i.em14,1))
                        if i.reproceso:
                            col8.append(round(i.reproceso,1))
                        else:
                            col8.append(0.0)
                        col8.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col8.append(round(i.humedad,1))
                        else:
                            col8.append(0.0)
                        if i.ph:
                            col8.append(round(i.ph,1))
                        else:
                            col8.append(0.0)
                    if x == 5:
                        col9 = list()
                        if 'MPDC00008' in col2:
                            col9.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col9.append(round(i.em2,1))
                            col9.append(round(i.em3,1))
                            col9.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col9.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col9.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col9.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col9.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col9.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col9.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col9.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col9.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col9.append(round(i.em14,1))
                        if i.reproceso:
                            col9.append(round(i.reproceso,1))
                        else:
                            col9.append(0.0)
                        col9.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col9.append(round(i.humedad,1))
                        else:
                            col9.append(0.0)
                        if i.ph:
                            col9.append(round(i.ph,1))
                        else:
                            col9.append(0.0)
                    if x == 6:
                        col10 = list()
                        if 'MPDC00008' in col2:
                            col10.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col10.append(round(i.em2,1))
                            col10.append(round(i.em3,1))
                            col10.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col10.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col10.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col10.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col10.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col10.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col10.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col10.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col10.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col10.append(round(i.em14,1))
                        if i.reproceso:
                            col10.append(round(i.reproceso,1))
                        else:
                            col10.append(0.0)
                        col10.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col10.append(round(i.humedad,1))
                        else:
                            col10.append(0.0)
                        if i.ph:
                            col10.append(round(i.ph,1))
                        else:
                            col10.append(0.0)
                    if x == 7:
                        col11 = list()
                        if 'MPDC00008' in col2:
                            col11.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col11.append(round(i.em2,1))
                            col11.append(round(i.em3,1))
                            col11.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col11.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col11.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col11.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col11.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col11.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col11.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col11.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col11.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col11.append(round(i.em14,1))
                        if i.reproceso:
                            col11.append(round(i.reproceso,1))
                        else:
                            col11.append(0.0)
                        col11.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col11.append(round(i.humedad,1))
                        else:
                            col11.append(0.0)
                        if i.ph:
                            col11.append(round(i.ph,1))
                        else:
                            col11.append(0.0)
                    if x == 8:
                        col12 = list()
                        if 'MPDC00008' in col2:
                            col12.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col12.append(round(i.em2,1))
                            col12.append(round(i.em3,1))
                            col12.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col12.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col12.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col12.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col12.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col12.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col12.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col12.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col12.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col12.append(round(i.em14,1))
                        if i.reproceso:
                            col12.append(round(i.reproceso,1))
                        else:
                            col12.append(0.0)
                        col12.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col12.append(round(i.humedad,1))
                        else:
                            col12.append(0.0)
                        if i.ph:
                            col12.append(round(i.ph,1))
                        else:
                            col12.append(0.0)
                    if x == 9:
                        col13 = list()
                        if 'MPDC00008' in col2:
                            col13.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col13.append(round(i.em2,1))
                            col13.append(round(i.em3,1))
                            col13.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col13.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col13.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col13.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col13.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col13.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col13.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col13.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col13.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col13.append(round(i.em14,1))
                        if i.reproceso:
                            col13.append(round(i.reproceso,1))
                        else:
                            col13.append(0.0)
                        col13.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col13.append(round(i.humedad,1))
                        else:
                            col13.append(0.0)
                        if i.ph:
                            col13.append(round(i.ph,1))
                        else:
                            col13.append(0.0)
                    if x == 10:
                        col14 = list()
                        if 'MPDC00008' in col2:
                            col14.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col14.append(round(i.em2,1))
                            col14.append(round(i.em3,1))
                            col14.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col14.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col14.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col14.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col14.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col14.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col14.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col14.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col14.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col14.append(round(i.em14,1))
                        if i.reproceso:
                            col14.append(round(i.reproceso,1))
                        else:
                            col14.append(0.0)
                        col14.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col14.append(round(i.humedad,1))
                        else:
                            col14.append(0.0)
                        if i.ph:
                            col14.append(round(i.ph,1))
                        else:
                            col14.append(0.0)
                    if x == 11:
                        col15 = list()
                        if 'MPDC00008' in col2:
                            col15.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col15.append(round(i.em2,1))
                            col15.append(round(i.em3,1))
                            col15.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col15.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col15.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col15.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col15.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col15.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col15.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col15.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col15.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col15.append(round(i.em14,1))
                        if i.reproceso:
                            col15.append(round(i.reproceso,1))
                        else:
                            col15.append(0.0)
                        col15.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col15.append(round(i.humedad,1))
                        else:
                            col15.append(0.0)
                        if i.ph:
                            col15.append(round(i.ph,1))
                        else:
                            col15.append(0.0)
                    if x == 12:
                        col16 = list()
                        if 'MPDC00008' in col2:
                            col16.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col16.append(round(i.em2,1))
                            col16.append(round(i.em3,1))
                            col16.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col16.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col16.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col16.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col16.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col16.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col16.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col16.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col16.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col16.append(round(i.em14,1))
                        if i.reproceso:
                            col16.append(round(i.reproceso,1))
                        else:
                            col16.append(0.0)
                        col16.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col16.append(round(i.humedad,1))
                        else:
                            col16.append(0.0)
                        if i.ph:
                            col16.append(round(i.ph,1))
                        else:
                            col16.append(0.0)                            
                    if x == 13:
                        col17 = list()
                        if 'MPDC00008' in col2:
                            col17.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col17.append(round(i.em2,1))
                            col17.append(round(i.em3,1))
                            col17.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col17.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col17.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col17.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col17.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col17.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col17.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col17.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col17.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col17.append(round(i.em14,1))
                        if i.reproceso:
                            col17.append(round(i.reproceso,1))
                        else:
                            col17.append(0.0)
                        col17.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col17.append(round(i.humedad,1))
                        else:
                            col17.append(0.0)
                        if i.ph:
                            col17.append(round(i.ph,1))
                        else:
                            col17.append(0.0)
                    if x == 14:
                        col18 = list()
                        if 'MPDC00008' in col2:
                            col18.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col18.append(round(i.em2,1))
                            col18.append(round(i.em3,1))
                            col18.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col18.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col18.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col18.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col18.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col18.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col18.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col18.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col18.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col18.append(round(i.em14,1))
                        if i.reproceso:
                            col18.append(round(i.reproceso,1))
                        else:
                            col18.append(0.0)
                        col18.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col18.append(round(i.humedad,1))
                        else:
                            col18.append(0.0)
                        if i.ph:
                            col18.append(round(i.ph,1))
                        else:
                            col18.append(0.0)
                    if x == 15:
                        col19 = list()
                        if 'MPDC00008' in col2:
                            col19.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col19.append(round(i.em2,1))
                            col19.append(round(i.em3,1))
                            col19.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col19.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col19.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col19.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col19.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col19.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col19.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col19.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col19.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col19.append(round(i.em14,1))
                        if i.reproceso:
                            col19.append(round(i.reproceso,1))
                        else:
                            col19.append(0.0)
                        col19.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col19.append(round(i.humedad,1))
                        else:
                            col19.append(0.0)
                        if i.ph:
                            col19.append(round(i.ph,1))
                        else:
                            col19.append(0.0)
                    if x == 16:
                        col20 = list()
                        if 'MPDC00008' in col2:
                            col20.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col20.append(round(i.em2,1))
                            col20.append(round(i.em3,1))
                            col20.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col20.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col20.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col20.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col20.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col20.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col20.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col20.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col20.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col20.append(round(i.em14,1))
                        if i.reproceso:
                            col20.append(round(i.reproceso,1))
                        else:
                            col20.append(0.0)
                        col20.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col20.append(round(i.humedad,1))
                        else:
                            col20.append(0.0)
                        if i.ph:
                            col20.append(round(i.ph,1))
                        else:
                            col20.append(0.0)
                    if x == 17:
                        col21 = list()
                        if 'MPDC00008' in col2:
                            col21.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col21.append(round(i.em2,1))
                            col21.append(round(i.em3,1))
                            col21.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col21.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col21.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col21.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col21.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col21.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col21.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col21.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col21.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col21.append(round(i.em14,1))
                        if i.reproceso:
                            col21.append(round(i.reproceso,1))
                        else:
                            col21.append(0.0)
                        col21.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col21.append(round(i.humedad,1))
                        else:
                            col21.append(0.0)
                        if i.ph:
                            col21.append(round(i.ph,1))
                        else:
                            col21.append(0.0)
                    if x == 18:
                        col22 = list()
                        if 'MPDC00008' in col2:
                            col22.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col22.append(round(i.em2,1))
                            col22.append(round(i.em3,1))
                            col22.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col22.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col22.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col22.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col22.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col22.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col22.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col22.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col22.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col22.append(round(i.em14,1))
                        if i.reproceso:
                            col22.append(round(i.reproceso,1))
                        else:
                            col22.append(0.0)
                        col22.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col22.append(round(i.humedad,1))
                        else:
                            col22.append(0.0)
                        if i.ph:
                            col22.append(round(i.ph,1))
                        else:
                            col22.append(0.0)
                    if x == 19:
                        col23 = list()
                        if 'MPDC00008' in col2:
                            col23.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col23.append(round(i.em2,1))
                            col23.append(round(i.em3,1))
                            col23.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col23.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col23.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col23.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col23.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col23.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col23.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col23.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col23.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col23.append(round(i.em14,1))
                        if i.reproceso:
                            col23.append(round(i.reproceso,1))
                        else:
                            col23.append(0.0)
                        col23.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col23.append(round(i.humedad,1))
                        else:
                            col23.append(0.0)
                        if i.ph:
                            col23.append(round(i.ph,1))
                        else:
                            col23.append(0.0)
                    if x == 20:
                        col24 = list()
                        if 'MPDC00008' in col2:
                            col24.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col24.append(round(i.em2,1))
                            col24.append(round(i.em3,1))
                            col24.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col24.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col24.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col24.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col24.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col24.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col24.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col24.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col24.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col24.append(round(i.em14,1))
                        if i.reproceso:
                            col24.append(round(i.reproceso,1))
                        else:
                            col24.append(0.0)
                        col24.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col24.append(round(i.humedad,1))
                        else:
                            col24.append(0.0)
                        if i.ph:
                            col24.append(round(i.ph,1))
                        else:
                            col24.append(0.0)


                    if x == 21:
                        col25 = list()
                        if 'MPDC00008' in col2:
                            col25.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col25.append(round(i.em2,1))
                            col25.append(round(i.em3,1))
                            col25.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col25.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col25.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col25.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col25.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col25.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col25.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col25.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col25.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col25.append(round(i.em14,1))
                        if i.reproceso:
                            col25.append(round(i.reproceso,1))
                        else:
                            col25.append(0.0)
                        col25.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col25.append(round(i.humedad,1))
                        else:
                            col25.append(0.0)
                        if i.ph:
                            col25.append(round(i.ph,1))
                        else:
                            col25.append(0.0)
                    if x == 22:
                        col26 = list()
                        if 'MPDC00008' in col2:
                            col26.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col26.append(round(i.em2,1))
                            col26.append(round(i.em3,1))
                            col26.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col26.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col26.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col26.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col26.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col26.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col26.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col26.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col26.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col26.append(round(i.em14,1))
                        if i.reproceso:
                            col26.append(round(i.reproceso,1))
                        else:
                            col26.append(0.0)
                        col26.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col26.append(round(i.humedad,1))
                        else:
                            col26.append(0.0)
                        if i.ph:
                            col26.append(round(i.ph,1))
                        else:
                            col26.append(0.0)
                    if x == 23:
                        col27 = list()
                        if 'MPDC00008' in col2:
                            col27.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col27.append(round(i.em2,1))
                            col27.append(round(i.em3,1))
                            col27.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col27.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col27.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col27.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col27.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col27.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col27.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col27.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col27.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col27.append(round(i.em14,1))
                        if i.reproceso:
                            col27.append(round(i.reproceso,1))
                        else:
                            col27.append(0.0)
                        col27.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col27.append(round(i.humedad,1))
                        else:
                            col27.append(0.0)
                        if i.ph:
                            col27.append(round(i.ph,1))
                        else:
                            col27.append(0.0)
                    if x == 24:
                        col28 = list()
                        if 'MPDC00008' in col2:
                            col28.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col28.append(round(i.em2,1))
                            col28.append(round(i.em3,1))
                            col28.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col28.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col28.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col28.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col28.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col28.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col28.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col28.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col28.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col28.append(round(i.em14,1))
                        if i.reproceso:
                            col28.append(round(i.reproceso,1))
                        else:
                            col28.append(0.0)
                        col28.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col28.append(round(i.humedad,1))
                        else:
                            col28.append(0.0)
                        if i.ph:
                            col28.append(round(i.ph,1))
                        else:
                            col28.append(0.0)
                    if x == 25:
                        col29 = list()
                        if 'MPDC00008' in col2:
                            col29.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col29.append(round(i.em2,1))
                            col29.append(round(i.em3,1))
                            col29.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col29.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col29.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col29.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col29.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col29.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col29.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col29.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col29.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col29.append(round(i.em14,1))
                        if i.reproceso:
                            col29.append(round(i.reproceso,1))
                        else:
                            col29.append(0.0)
                        col29.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col29.append(round(i.humedad,1))
                        else:
                            col29.append(0.0)
                        if i.ph:
                            col29.append(round(i.ph,1))
                        else:
                            col29.append(0.0)
                    if x == 26:
                        col30 = list()
                        if 'MPDC00008' in col2:
                            col30.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col30.append(round(i.em2,1))
                            col30.append(round(i.em3,1))
                            col30.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col30.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col30.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col30.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col30.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col30.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col30.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col30.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col30.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col30.append(round(i.em14,1))
                        if i.reproceso:
                            col30.append(round(i.reproceso,1))
                        else:
                            col30.append(0.0)
                        col30.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col30.append(round(i.humedad,1))
                        else:
                            col30.append(0.0)
                        if i.ph:
                            col30.append(round(i.ph,1))
                        else:
                            col30.append(0.0)
                    if x == 27:
                        col31 = list()
                        if 'MPDC00008' in col2:
                            col31.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col31.append(round(i.em2,1))
                            col31.append(round(i.em3,1))
                            col31.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col31.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col31.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col31.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col31.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col31.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col31.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col31.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col31.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col31.append(round(i.em14,1))
                        if i.reproceso:
                            col31.append(round(i.reproceso,1))
                        else:
                            col31.append(0.0)
                        col31.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col31.append(round(i.humedad,1))
                        else:
                            col31.append(0.0)
                        if i.ph:
                            col31.append(round(i.ph,1))
                        else:
                            col31.append(0.0)
                    if x == 28:
                        col32 = list()
                        if 'MPDC00008' in col2:
                            col32.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col32.append(round(i.em2,1))
                            col32.append(round(i.em3,1))
                            col32.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col32.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col32.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col32.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col32.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col32.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col32.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col32.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col32.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col32.append(round(i.em14,1))
                        if i.reproceso:
                            col32.append(round(i.reproceso,1))
                        else:
                            col32.append(0.0)
                        col32.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col32.append(round(i.humedad,1))
                        else:
                            col32.append(0.0)
                        if i.ph:
                            col32.append(round(i.ph,1))
                        else:
                            col32.append(0.0)
                    if x == 29:
                        col33 = list()
                        if 'MPDC00008' in col2:
                            col33.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col33.append(round(i.em2,1))
                            col33.append(round(i.em3,1))
                            col33.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col33.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col33.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col33.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col33.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col33.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col33.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col33.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col33.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col33.append(round(i.em14,1))
                        if i.reproceso:
                            col33.append(round(i.reproceso,1))
                        else:
                            col33.append(0.0)
                        col33.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col33.append(round(i.humedad,1))
                        else:
                            col33.append(0.0)
                        if i.ph:
                            col33.append(round(i.ph,1))
                        else:
                            col33.append(0.0)
                    if x == 30:
                        col34 = list()
                        if 'MPDC00008' in col2:
                            col34.append(round(i.em1,1))
                        if 'MPDC00004' in col2:
                            col34.append(round(i.em2,1))
                            col34.append(round(i.em3,1))
                            col34.append(round(i.em4,1))
                        if 'MPDC00002' in col2:
                            col34.append(round(i.em5,1))
                        if 'AGUA' in col2:
                            col34.append(round(i.em6,1))
                        if 'SE-NEUT001' in col2:
                            col34.append(round(i.em7,1))
                        if 'MPCL00002' in col2:
                            col34.append(round(i.em8,1))
                        if 'MPC000022' in col2:
                            col34.append(round(i.em9,1))
                        if 'MPD000044' in col2:
                            col34.append(round(i.em10,1))
                        if 'MPC000022' in col2:
                            col34.append(round(i.em11,1))
                        if 'MPC000025' in col2:
                            col34.append(round(i.em15,1))
                        if 'MPC000030' in col2:
                            col34.append(round(i.em14,1))
                        if i.reproceso:
                            col34.append(round(i.reproceso,1))
                        else:
                            col34.append(0.0)
                        col34.append(round(i.receta_total_kg,1))
                        if i.humedad:
                            col34.append(round(i.humedad,1))
                        else:
                            col34.append(0.0)
                        if i.ph:
                            col34.append(round(i.ph,1))
                        else:
                            col34.append(0.0)

                    x += 1

                if 'MPDC00008' in col2:    
                    colt.append(round(totem1,1))
                if 'MPDC00004' in col2:
                    colt.append(round(totem2,1))
                    colt.append(round(totem3,1))
                    colt.append(round(totem4,1))
                if 'MPDC00002' in col2:
                    colt.append(round(totem5,1))
                if 'AGUA' in col2:    
                    colt.append(round(totem6,1))
                if 'SE-NEUT001' in col2:
                    colt.append(round(totem7,1))
                if 'MPCL00002' in col2:    
                    colt.append(round(totem8,1))
                if 'MPC000022' in col2:    
                    colt.append(round(totem9,1))
                if 'MPD000044' in col2:    
                    colt.append(round(totem10,1))
                if 'MPC000022' in col2:
                    colt.append(round(totem11,1))
                if 'MPC000025' in col2:    
                    colt.append(round(totem15,1))
                if 'MPC000030' in col2:    
                    colt.append(round(totem14,1))
                colt.append(round(totrep,1))
                total = totem1+totem2+totem3+totem4+totem5+totem6+totem7+totem8+totem9+totem10+totem11+totem14+totem15+totrep                
                colt.append(round(total,1))

                if y > 0:
                    totaly = tothum/y
                else:
                    totaly = 0.0
                if z > 0:
                    totalz = totph/z
                else:
                    totalz = 0.0
                colt.append(round(totaly,1))
                colt.append(round(totalz,1))
        else:
            nolista2 = 0

        if nolista2 == 0:
            #print("No hay datos")
            resultado = zip(col1,col2,col3,col4)
        elif nolista2 == 1:    
            resultado = zip(col1,col2,col3,col4,col5,colt)
        elif nolista2 == 2:   
            resultado = zip(col1,col2,col3,col4,col5,col6,colt)
        elif nolista2 == 3:   
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,colt)
        elif nolista2 == 4:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,colt)
        elif nolista2 == 5:    
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,colt)
        elif nolista2 == 6:          
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,colt)
        elif nolista2 == 7:        
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,colt)
        elif nolista2 == 8:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,colt)        
        elif nolista2 == 9:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,colt)
        elif nolista2 == 10:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,colt)
        elif nolista2 == 11:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,colt)
        elif nolista2 == 12:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,colt)            
        elif nolista2 == 13:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,colt)
        elif nolista2 == 14:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,colt)
        elif nolista2 == 15:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,colt)
        elif nolista2 == 16:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,colt)
        elif nolista2 == 17:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,colt)
        elif nolista2 == 18:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,colt)
        elif nolista2 == 19:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,colt)
        elif nolista2 == 20:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,colt)
        elif nolista2 == 21:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,colt)
        elif nolista2 == 22:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,colt)
        elif nolista2 == 23:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,colt)
        elif nolista2 == 24:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,colt)
        elif nolista2 == 25:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,colt)
        elif nolista2 == 26:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,colt)
        elif nolista2 == 27:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,col31,colt)
        elif nolista2 == 28:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,col31,col32,colt)
        elif nolista2 == 29:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,col31,col32,col33,colt)
        elif nolista2 >= 30:
            resultado = zip(col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11,col12,col13,col14,col15,col16,col17,col18,col19,col20,col21,col22,col23,col24,col25,col26,col27,col28,col29,col30,col31,col32,col33,col34,colt)
        return resultado                                                                                     
        # ********************************************    
        # Fin de la creacion de las lista del curpo de
        # la tabla
        # ********************************************              