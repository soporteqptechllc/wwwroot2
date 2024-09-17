from django.contrib import admin
from .models import planta, silosML, silos, pedidos, Valoressensores, llegadas,material

admin.site.site_header = "Argos Panamá, S.A. - Pedidos Automáticos"
admin.site.site_title = "Portal de Pedidos Automáticos de Argos Panamá, S.A."
admin.site.index_title = "Bienvenidos al portal de administración"

# Register your models here.
# admin.site.register(silos)
#admin.site.register(pedidos)
admin.site.register(silosML)
admin.site.register(planta)
#admin.site.register(Valoressensores)
#admin.site.register(llegadas)

@admin.register(material)
class materialAdmin(admin.ModelAdmin):
    list_display = ("id","codigo_sap", "nombre_material", "nombre_corto","densidad")
    ordering = ('codigo_sap',)
    search_fields = ("id","codigo_sap", "nombre_material", "nombre_corto","densidad")
    list_filter = ("id","codigo_sap", "nombre_material", "nombre_corto","densidad") 

@admin.register(silos)
class silosAdmin(admin.ModelAdmin):
    list_display = ("id","planta","silo","codigo_sap","metros", "nivel", "toneladas","altura_cilindro","setpoint","metrosxbotella","radio_cilindro","ultimo_llenado")
    ordering = ('planta','silo')
    search_fields = ("id","planta","silo","codigo_sap","metros", "nivel", "toneladas","altura_cilindro","setpoint","metrosxbotella","radio_cilindro")
    list_filter = ("planta","silo","codigo_sap") 


@admin.register(Valoressensores)
class ValoressensoresAdmin(admin.ModelAdmin):
    list_display = ("fecha", "hora","origen","nombre_silo","nivel", "descripcion","id")
    ordering = ('-fecha','-hora')
    search_fields = ("origen", "nombre_silo","fecha","id")
    list_filter = ("origen","nombre_silo")

@admin.register(pedidos)
class pedidosAdmin(admin.ModelAdmin):
    list_display = ("id","fecha_pedido","planta","nom_silo","description","codigo_sap","nivel_metros","decremento","pedidos_id", "nivel_porcen", "prioridad","id_tablaLlegadas","id_sensorP")
    ordering = ('-fecha_pedido',)
    search_fields = ("id","fecha_pedido","planta","nom_silo","pedidos_id", "nivel_porcen", "prioridad","id_tablaLlegadas","id_sensorP")
    list_filter = ("planta","nom_silo")


@admin.register(llegadas)
class llegadasAdmin(admin.ModelAdmin):
    list_display = ("id","planta","nom_silo","fecha_min","fecha_fin","n_minimo","n_maximo","incremento","id_sensorLL","nivel_porcen","llegadas_id","description")
    ordering = ('-fecha_min',)
    search_fields = ("id","planta","nom_silo","fecha_min","fecha_fin","n_minimo","n_maximo","incremento","id_sensorLL","nivel_porcen","llegadas_id","description")
    list_filter = ("planta","nom_silo","llegadas_id","description")
