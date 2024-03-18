# Import Django
from django.contrib import admin
# Local Models
from .models import (
    ReporteLAB,
    )
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

# Register your models here.
admin.site.site_header = "Argos Panamá, S.A. - Django administration"
#admin.site.site_title = "Portal de Pedidos Automáticos de Argos Panamá, S.A."
admin.site.index_title = "Bienvenidos al portal de administración" 

# Defino los titulos de las columnas de el admin. de Django
class ReporteLaboratorioAdmin(admin.ModelAdmin):
    list_display = (
        'id','tipo','datetime','cemento'
        )
    search_fields =(
        'datetime',
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'id','tipo','datetime','productoid'
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('tipo','cemento',)
    # Permite filtrar por campos tipo fecha
    date_hierarchy = 'datetime'
    # Permite limitar el numero de filas a ver por pagina
    list_per_page = 25
    # Perminte limitar el numero maximo de registro por pantalla
    # list_max_show_all = 200
admin.site.register(ReporteLAB,ReporteLaboratorioAdmin)