# Import admin Django
from django.contrib import admin

# Import Model Django
from .models import (
    productos,
    boquillas,
    mezclado,
    )

# Register your models here.

# Defino los titulos de las columnas del admin. de Django
class ProductosAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_Producto',
        'name',
        'peso'
        )
    search_fields =(
        'id_Producto',
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'id_Producto',
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = ('id_Producto',)

admin.site.register(productos,ProductosAdmin)

class BoquillasAdmin(admin.ModelAdmin):
    
    list_display = (
        'id',
        'n_boquilla',
        'id_producto',
        'idbq',
        'datetime_plc',

        )
    search_fields =(
        'id',
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'id',
    )
    # Permite filtrar los registros o filas en la tabla
    #list_filter = ('id',)
        
admin.site.register(boquillas,BoquillasAdmin) 

# Defino los titulos de las columnas del admin. de Django
class mezcladoAdmin(admin.ModelAdmin):
    list_display = (
        'batch_id'      ,
        'lote'         ,
        'id_producto'   ,
        'name_producto' ,
        'silo1' ,
        'silo2' ,
        'silo3' ,
        'silo4' ,
        'silo5' ,
        'silo6' ,
        'silo7' ,
        'silo8' ,
        'year_start'    ,
        'month_start'   ,
        'day_start'     ,
        'hour_start'    ,
        'minute_start' ,
        'second_start'  ,
        'year_end'      ,
        'month_end'     ,
        'day_end'       ,
        'hour_end'    ,
        'minute_end'    ,
        'second_end'   ,
        'bz_agre1_sp'   ,
        'bz_agre1_pv'   ,
        'bz_agre2_sp'   ,
        'bz_agre2_pv'  ,
        'bz_agre3_sp'   ,
        'bz_agre3_pv'   ,
        'bz_agre4_sp' ,
        'bz_agre4_pv'   ,
        'bz_cem1_sp'    ,
        'bz_cem1_pv'    ,
        'bz_cem2_sp'    ,
        'bz_cem2_pv'    ,
        'bz_adit_sp'    ,
        'bz_adit_pv'   ,
        'time_mezcla'   ,

        )
    search_fields =(
        'batch_id'      ,
        'lote'         ,
        'id_producto'   ,
        'name_producto' ,
    )
    # Permite ordenar por una o mas columnas
    ordering = (
        'batch_id'      ,
        'lote'         ,
        'id_producto'   ,
        'name_producto' ,
    )
    # Permite filtrar los registros o filas en la tabla
    list_filter = (
        'batch_id'      ,
        'lote'         ,
        'id_producto'   ,
        'name_producto' ,
        )

admin.site.register(mezclado,mezcladoAdmin)