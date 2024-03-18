from django.contrib import admin

# Register your models here.
from .models import Empresa,Responsables,CentroDeCostos,Ingenieros,encabezado,reportehoras, producciondiaria

# Register your models here.

admin.site.register(Empresa)
admin.site.register(Responsables)
admin.site.register(CentroDeCostos)
admin.site.register(Ingenieros)
admin.site.register(encabezado)
admin.site.register(reportehoras)
admin.site.register(producciondiaria)