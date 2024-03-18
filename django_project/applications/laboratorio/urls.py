"""
URLS DEL APP LABORATORIO - API REST
"""
# Django
from django.urls import path
# Local
from . import views

app_name = 'laboratorio_app'
urlpatterns = [
     # ****************************************************** 
     # ****************************************************** 
    # REPORTE DE LABORATORIO
     # URL - lista de reportes de laboratorio semielaborados
     path('laboratorio/api-rango-fecha-reportelab/<fecha1>/<fecha2>/',
         views.ListaReporteLAB_API1.as_view(), name='reportelab_range_fecha'),
    path('laboratorio/api-rango-fecha-reportelab2/<fecha1>/<fecha2>/',
         views.ListaReporteLAB_API2.as_view(), name='reportelab_range_fecha'),
]