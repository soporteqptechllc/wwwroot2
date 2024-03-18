# Import Model Django
from django.db import models
from django.utils import timezone
# Create your models here.

# Tabla de Productos
class productos(models.Model):
    id_Producto = models.IntegerField('id_Producto', unique=True)
    name = models.CharField('name_Producto', max_length=60, unique=True)
    peso = models.FloatField('peso_kg', blank=True, null=True)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Producto'  # Nombre de Columna singular
      verbose_name_plural = 'Productos'  # Nombre en plural

      # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id_Producto)
    
# Tabla de Boquillas
class boquillas(models.Model):
    n_boquilla = models.IntegerField('#_boquilla',blank=True, null=True)
    id_producto = models.ForeignKey(productos, on_delete=models.CASCADE, related_name='id_producto')
    name_producto = models.CharField('name_Producto', max_length=60, blank=True, null=True)
    idbq = models.BigIntegerField('idBQ',blank=True, null=True)
    sp = models.FloatField('setpoint', blank=True, null=True)
    peso = models.FloatField('peso_kg', blank=True, null=True)
    sp_ajuste1 = models.FloatField('sp_ajuste1', blank=True, null=True)
    sp_ff = models.FloatField('sp_ajuste2', blank=True, null=True)
    year = models.IntegerField('año',blank=True, null=True)
    mes = models.IntegerField('mes',blank=True, null=True)
    dia = models.IntegerField('dia',blank=True, null=True)
    hora = models.IntegerField('hora',blank=True, null=True)
    min = models.IntegerField('min',blank=True, null=True)
    seg = models.IntegerField('seg',blank=True, null=True)
    datetime_plc = models.DateTimeField('datatime_plc', blank=True, null=True)

    # Funciones adicional para, busca la descripcion del Producto por su id
    def save(self, *args, **kwargs):
      # Buscar la descripcion 
      DesProd = None                           
      if self.id_producto:
         id_prod = int(str(self.id_producto))  
         des_prod = productos.objects.filter(id_Producto = id_prod).values()
         if des_prod:
            DesProd = des_prod[0]['name']
         else:
            DesProd = None 
      self.name_producto = DesProd         
      super(boquillas,self).save(*args,**kwargs)

    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Boquilla'  # Nombre de Columna singular
      verbose_name_plural = 'Boquillas'  # Nombre en plural

    # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + str(self.n_boquilla) + ' - ' + str(self.idbq)
    
# Tabla de Mezclado
class mezclado(models.Model):
    batch_id      = models.IntegerField('batch_id',blank=True, null=True)
    lote          = models.IntegerField('lote',blank=True, null=True)
    id_producto   = models.ForeignKey(productos, on_delete=models.CASCADE, related_name='id_producto2')
    name_producto = models.CharField('name_Producto', max_length=60, blank=True, null=True)
    silo1 = models.FloatField('silo1', blank=True, null=True)
    silo2 = models.FloatField('silo2', blank=True, null=True)
    silo3 = models.FloatField('silo3', blank=True, null=True)
    silo4 = models.FloatField('silo4', blank=True, null=True)
    silo5 = models.FloatField('silo5', blank=True, null=True)
    silo6 = models.FloatField('silo6', blank=True, null=True)
    silo7 = models.FloatField('silo7', blank=True, null=True)
    silo8 = models.FloatField('silo8', blank=True, null=True)
    year_start    = models.IntegerField('year_start',blank=True, null=True)
    month_start   = models.IntegerField('month_start',blank=True, null=True)
    day_start     = models.IntegerField('day_start',blank=True, null=True)
    hour_start    = models.IntegerField('hour_start',blank=True, null=True)
    minute_start  = models.IntegerField('minute_start',blank=True, null=True)
    second_start  = models.IntegerField('second_start',blank=True, null=True)
    year_end      = models.IntegerField('year_end',blank=True, null=True)
    month_end     = models.IntegerField('month_end',blank=True, null=True)
    day_end       = models.IntegerField('day_end',blank=True, null=True)
    hour_end      = models.IntegerField('hour_end',blank=True, null=True)
    minute_end    = models.IntegerField('minute_end',blank=True, null=True)
    second_end    = models.IntegerField('second_end',blank=True, null=True)
    bz_agre1_sp   = models.FloatField('bz_agre1_sp', blank=True, null=True)
    bz_agre1_pv   = models.FloatField('bz_agre1_pv', blank=True, null=True)
    bz_agre2_sp   = models.FloatField('bz_agre2_sp', blank=True, null=True)
    bz_agre2_pv   = models.FloatField('bz_agre2_pv', blank=True, null=True)
    bz_agre3_sp   = models.FloatField('bz_agre3_sp', blank=True, null=True)
    bz_agre3_pv   = models.FloatField('bz_agre3_pv', blank=True, null=True)
    bz_agre4_sp   = models.FloatField('bz_agre4_sp', blank=True, null=True)
    bz_agre4_pv   = models.FloatField('bz_agre4_pv', blank=True, null=True)
    bz_cem1_sp    = models.FloatField('bz_cem1_sp', blank=True, null=True)
    bz_cem1_pv    = models.FloatField('bz_cem1_pv', blank=True, null=True)
    bz_cem2_sp    = models.FloatField('bz_cem2_sp', blank=True, null=True)
    bz_cem2_pv    = models.FloatField('bz_cem2_pv', blank=True, null=True)
    bz_adit_sp    = models.FloatField('bz_adit_sp', blank=True, null=True)
    bz_adit_pv    = models.FloatField('bz_adit_pv', blank=True, null=True)
    time_mezcla   = models.FloatField('time_mezcla', blank=True, null=True)
    total_sp      = models.FloatField('total_sp kg', blank=True, null=True)
    total_pv      = models.FloatField('total_pv kg', blank=True, null=True) 
    total_ton      = models.FloatField('total_ton ton', blank=True, null=True)
    datetime_plc = models.DateTimeField('datatime_plc', blank=True, null=True)
    # Funciones adicionales para modificar los registros y realizar sumas
    def save(self, *args, **kwargs):        
        # Sumo los SP, PV y calculo las Toneladas
        d_sp = round(self.bz_agre1_sp+self.bz_agre2_sp+self.bz_agre3_sp+self.bz_agre4_sp+self.bz_cem1_sp+self.bz_cem2_sp+self.bz_adit_sp,3)
        d_pv = round(self.bz_agre1_pv+self.bz_agre2_pv+self.bz_agre3_pv+self.bz_agre4_pv+self.bz_cem1_pv+self.bz_cem2_pv+self.bz_adit_pv,3)
        d_ton = round(d_pv/1000,3)        
        self.total_sp = d_sp
        self.total_pv = d_pv
        self.total_ton = d_ton
        super(mezclado,self).save(*args,**kwargs)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Mesclado'  # Nombre de Columna singular
      verbose_name_plural = 'Mesclados'  # Nombre en plural
    # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + str(self.batch_id) 