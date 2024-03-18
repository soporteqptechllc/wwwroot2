"""
URLS FROM BOQUILLAS
"""
from django.urls import path
from . import views

app_name = 'boquillas_app'
urlpatterns = [
    #path('', views.InicioView.as_view(), name='inicio'),
    path('boquillas/listar_boquillas_all/', views.ListBoquillasAll.as_view(), name='boquillas_all'),
    path('boquillas/listar_boquillas/<int:kword>/',views.ListBoquillaView.as_view(),name='list_boquilla'),
    path('boquillas/inf_ensacado/',views.ResumenDiarioView.as_view(),name='inf_ensacado'),
    path('boquillas/inf_mezclado/',views.ResumenDiarioMezcladoView.as_view(),name='inf_mezclado'),
    path('boquillas/inf_mezcladoEmail/<str:fecha>/<int:excelE>/',views.CrearArchivoExcel.as_view(),name='inf_mezcladoExcel'),
]