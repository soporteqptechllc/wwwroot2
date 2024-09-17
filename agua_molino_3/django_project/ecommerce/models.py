from django.db import models
from django.db.models.deletion import CASCADE

# # Create your models here.
# class FiltroInventario(models.Model):
#     Material = models.IntegerField()
#     TextoBreve = models.CharField(max_length=260)
#     Stock = models.IntegerField()
#     def __str__(self):
#         return f"{self.Material}:  {self.TextoBreve} : {self.Stock}"


class inventario(models.Model):
    unnamed_0 = models.FloatField(db_column='Unnamed: 0', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    saldo_al = models.TextField(db_column='Saldo al', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    soc_field = models.TextField(db_column='Soc.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    cta_mayor = models.BigIntegerField(db_column='Cta.mayor', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material = models.BigIntegerField(db_column='Material', blank=True, null=False)  # Field name made lowercase.
    texto_breve_de_material = models.TextField(db_column='Texto breve de material', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_stock_total = models.TextField(db_column='       Stock total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    umb = models.TextField(db_column='UMB', blank=True, null=True)  # Field name made lowercase.
    precio_variable = models.TextField(db_column='Precio variable', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    field_valor_total = models.TextField(db_column='       Valor total', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    catva = models.BigIntegerField(db_column='CatVa', blank=True, null=True)  # Field name made lowercase.
    prc = models.TextField(db_column='Prc', blank=True, null=True)  # Field name made lowercase.
    field_por = models.BigIntegerField(db_column='   por', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    mon_field = models.TextField(db_column='Mon.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    tipval = models.TextField(db_column='TipVal', blank=True, null=True)  # Field name made lowercase.
    
    def __str__(self):
        return f"Material #:{self.material}/  Descripcion :{self.texto_breve_de_material} / Stock : {self.field_stock_total} "



    class Meta:
        managed = True
        db_table = 'inventario'

class molino3(models.Model):
    #id = models.AutoField(primary_key=True)
    area_de_planta = models.TextField(db_column='AREA DE PLANTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion_funcional = models.TextField(db_column='UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion_de_ubicacion_funcional = models.TextField(db_column='DESCRIPCION DE UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    equipo = models.TextField(db_column='EQUIPO', blank=True, null=True)  # Field name made lowercase.
    equipo_hac = models.TextField(db_column='EQUIPO_HAC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #material = models.BigIntegerField(db_column='Material', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material= models.ForeignKey(inventario, on_delete=CASCADE, related_name="repuesto")
    descripcion_de_material = models.TextField(db_column='DESCRIPCION DE MATERIAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cant_field = models.FloatField(db_column='CANT.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unidad_de_medida = models.TextField(db_column='UNIDAD DE MEDIDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    #repuesto = models.ForeignKey(inventario, to_field='material', on_delete=CASCADE)

    def __str__(self):
        #return "Material: "+self.material+"  Equipo: "+self.equipo_hac
        return f"Area:{self.descripcion_de_ubicacion_funcional}/  Equipo:{self.equipo_hac} / Repuesto: {self.material} "


    class Meta:
        managed = True
        db_table = 'molino3'


class equipos(models.Model):
    area_de_planta = models.TextField(db_column='AREA DE PLANTA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ubicacion_funcional = models.TextField(db_column='UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion_de_ubicacion_funcional = models.TextField(db_column='DESCRIPCION DE UBICACION FUNCIONAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    equipo = models.TextField(db_column='EQUIPO', blank=True, null=True)  # Field name made lowercase.
    equipo_hac = models.TextField(db_column='EQUIPO_HAC', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    material= models.ForeignKey(inventario, on_delete=CASCADE, related_name="repuesto2")
    descripcion_de_material = models.TextField(db_column='DESCRIPCION DE MATERIAL', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cant_field = models.FloatField(db_column='CANT.', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    unidad_de_medida = models.TextField(db_column='UNIDAD DE MEDIDA', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        #return "Material: "+self.material+"  Equipo: "+self.equipo_hac
        return f"Area:{self.descripcion_de_ubicacion_funcional}/  Equipo:{self.equipo_hac} / Repuesto: {self.material} "


    class Meta:
        managed = True
        db_table = 'equipos'