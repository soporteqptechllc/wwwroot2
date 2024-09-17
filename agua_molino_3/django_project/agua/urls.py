"""
URLS DE EL APP API REST
"""
# Django
from django.urls import path
# Local
from . import views

app_name = 'agua_app'
urlpatterns = [
     # ****************************************************** 
     # ******************************************************
     # MEDICIONES DE AGUA DE RIO
     # HTML - Lista los datos de la mediciones del agua de rio en general
     path('rio/lista_mediciones_agua/',
          views.ListMedicionesAguaRio.as_view(), name='mediciones_agua_lista'),
    # HTML - Grafica de los datos de la mediciones del agua de rio en general
     path('rio/grafica_mediciones_agua_v/',
          views.GraficaMedicionAguaRio1.as_view(), name='mediciones_agua_grafica1'),
    # HTML - Grafica de los datos de la mediciones del agua de rio en general
     path('rio/grafica_mediciones_agua_f/',
          views.GraficaMedicionAguaRio2.as_view(), name='mediciones_agua_grafica2'),
    # URL - Lista de mediciones de agua de rio en general
     path('rio/api_lista_mediciones_agua/', 
          views.ListMedicionesAguaRioAPI.as_view(), name='api_mediciones_agua_lista'),
    # URL - Creacion de una medicion de agua de rio 
     path('rio/api_crear_medicion_agua/',
         views.CrearMedicionesAguaRioAPI.as_view(), name='api_medicion_agua_create'),
     # ****************************************************** 
     # ******************************************************
     # MEDICIONES DE AGUA DE LANZAS DE MOLINO3
    # URL - Creacion de una medicion de agua de rio 
     path('lanzasMolino3/api_crear_medicion_agua_lanzas_molino3/',
         views.CrearMedidorAguaLanzasMolino3API.as_view(), name='api_medicion_agua_lanzas_molino3_create'),     
    # HTML - Grafica de los datos del consumo del agua de Lanzas de Molino 3 ANUAL
     path('lanzasMolino3/grafica_consumo_agua_lanzas_molino3a/<int:ano>/<int:email>',
          views.GraficaConsumoAguaLanzasM3A.as_view(), name='consumo_agua_lanzas_m3a_grafica'),
    # HTML - Grafica de los datos del consumo del agua de Lanzas de Molino 3 SEMANAL
     path('lanzasMolino3/grafica_consumo_agua_lanzas_molino3s/<int:ano>/<int:semana>/',
          views.GraficaConsumoAguaLanzasM3S.as_view(), name='consumo_agua_lanzas_m3s_grafica'),
]   