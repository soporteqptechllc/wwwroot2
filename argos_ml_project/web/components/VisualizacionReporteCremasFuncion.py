#from django.contrib.auth.models import Group
#from allauth.account.models import EmailAddress # VALIDAR EMAIL NO VA (JG)
# C:\QPTECH\aalvarado\django_sap\VisualizacionReporteCremas.py
#from django.db import models
import os
import django
import datetime
import pandas as pd
def ActualizaReporte(fecha):
    # project_name nombre del proyecto
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_sap.settings.base")
    django.setup()
    from applications.api.models import operaciones
    from web.components.models import producciondiaria

    # Lee la base de datos de reportes de batchs 
    batchs = operaciones.objects.last()
    ultimoRegistro = int(batchs.hora[0:20].replace(" ", "").replace(":","").replace("-",""))
    #print(ultimoRegistro)
    hoy = datetime.datetime.today()
    ems = ['em1','em2','em3','em4','em5','em6','em7','em8','em9','em15','em14']
    #fecha = '20230803'
    viewOper = operaciones.objects.filter(hora__contains = fecha).order_by('id')
    listViewOper = list(viewOper.values())
    producciondiaria.objects.all().update(
        setpoint = 0,
        op1  = 0,
        op2 =  0,
        op3 =  0,
        op4 =  0,
        op5 =  0,
        op6 =  0,
        op7 =  0,
        op8 =  0,
        op9 =  0,
        op10 =  0,
        op11 =  0,
        op12 =  0,
        op13 =  0,
        op14 =  0,
        op15 =  0,
        op16 =  0,
        op17 =  0,
        op18 =  0,
        op19 =  0,
        op20 =  0,
        total =  0,
    )
    produccionDia = producciondiaria.objects.all().order_by('id')
    #print(len(produccionDia), len(listViewOper))
    #print(produccionDia)
    #print(listViewOper)
    romper = len(listViewOper)
    totalGeneral = 0
    k = 0



    totop1 = totop2 = totop3 = totop4 = totop5 = totop6 =0
    totop7 = totop8 = totop9 = totop10 = totop11 = totop12 =0
    totop13 = totop14 = totop15 = totop16 = totop17 = totop18 =0
    totop19 = totop20 =0

    for i in produccionDia:
        if k<=13:
            # print(k,"   ",listViewOper[0][ems[k]])
            if romper >= 1 :
                i.op1 = listViewOper[0][ems[k]]
                totop1 += i.op1
            if romper >= 2 :
                i.op2 = listViewOper[1][ems[k]]
                totop2 += i.op2
            if romper >= 3 :
                i.op3 = listViewOper[2][ems[k]]
                totop3 += i.op3
            if romper >= 4 :
                i.op4 = listViewOper[3][ems[k]]
                totop4 += i.op4
            if romper >= 5 :
                i.op5 = listViewOper[4][ems[k]]
                totop5 += i.op5
            if romper >= 6 :
                i.op6 = listViewOper[5][ems[k]]
                totop6 += i.op6
            if romper >= 7 :
                i.op7 = listViewOper[6][ems[k]]
                totop7 += i.op7
            if romper >= 8 :
                i.op8 = listViewOper[7][ems[k]]
                totop8 += i.op8
            if romper >= 9 :
                i.op9 = listViewOper[8][ems[k]]
                totop9 += i.op9
            if romper >= 10 :
                i.op10 = listViewOper[9][ems[k]]
                totop10 += i.op10
            if romper == 11 :
                i.op11 = listViewOper[10][ems[k]]
                totop11 += i.op11
            if romper >= 12 :
                i.op12 = listViewOper[11][ems[k]]
                totop12 += i.op12
            if romper >= 13 :
                i.op13 = listViewOper[12][ems[k]]
                totop13 += i.op13
            if romper >= 14 :
                i.op14 = listViewOper[13][ems[k]]
                totop14 += i.op14
            if romper >= 15 :
                i.op15 = listViewOper[14][ems[k]]
                totop15 += i.op15
            if romper >= 16 :
                i.op16 = listViewOper[15][ems[k]]
                totop16 += i.op16
            if romper >= 17 :
                i.op17 = listViewOper[16][ems[k]]
                totop17 += i.op17
            if romper >= 18 :
                i.op18 = listViewOper[17][ems[k]]
                totop18 += i.op18
            if romper >= 19 :
                i.op19 = listViewOper[18][ems[k]]
                totop19 += i.op19
            if romper >= 20 :
                i.op20 = listViewOper[19][ems[k]]
                totop20 += i.op20
            
            i.total = i.op1+i.op2+i.op3+i.op4+i.op5+i.op6+i.op7+i.op8+i.op9+i.op10+i.op11+i.op12+i.op13+i.op14+i.op15+i.op16+i.op17+i.op18+i.op19+i.op20
            totalGeneral = totalGeneral + i.total

        i.save()
        k= k+1
        
    filaTotales = producciondiaria.objects.get(pk =12)
    filaTotales.op1 = totop1
    filaTotales.op2 = totop2
    filaTotales.op3 = totop3
    filaTotales.op4 = totop4
    filaTotales.op5 = totop5
    filaTotales.op6 = totop6
    filaTotales.op7 = totop7
    filaTotales.op8 = totop8
    filaTotales.op9 = totop9
    filaTotales.op10 = totop10
    filaTotales.op11 = totop11
    filaTotales.op12 = totop12
    filaTotales.op13 = totop13
    filaTotales.op14 = totop14
    filaTotales.op15 = totop15
    filaTotales.op16 = totop16
    filaTotales.op17 = totop17
    filaTotales.op18 = totop18
    filaTotales.op19 = totop19
    filaTotales.op20 = totop20
    filaTotales.total =totalGeneral

    filaTotales.save()
