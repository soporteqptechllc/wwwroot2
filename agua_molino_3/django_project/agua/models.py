# Import Model Django
from django.db import models

# Import Local Managers
from .managers import MedidorAguaRioManager, MedidorAguaLanzasMolino3Manager

# Create your models here.

# ***********************************************************************************  
class MedidorAguaRio(models.Model):
    created_at = models.DateTimeField(db_column='datatime_db',auto_now=True)
    datatime = models.DateTimeField(db_column='datatime_plc', blank=True, null=True)
    volumen = models.PositiveIntegerField(db_column='volumen_totalizado',default=0)
    flujo = models.FloatField(db_column='medida_flujo',default=0)
    nivel = models.FloatField(db_column='nivel_tanq',default=0)
    bomba1 = models.PositiveIntegerField(db_column='estado_bomba1',default=0)
    bomba2 = models.PositiveIntegerField(db_column='estado_bomba2',default=0)
    # Importo modelos avanzados de Manager
    objects = MedidorAguaRioManager()
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'MedidorDeAguaRio'  # Nombre de Columna singular
      verbose_name_plural = 'MedidasDeAguaDeRio'  # Nombre en plural
    # Defino los titulos de las columnas del admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + str(self.created_at) + ' - ' + str(self.volumen) + ' - ' + str(self.flujo) + ' - ' + str(self.nivel)

class MedidorAguaLanzasMolino3(models.Model):
    created_at = models.DateTimeField(db_column='datatime_db',auto_now=True)
    volumen = models.PositiveIntegerField(db_column='volumen_totalizado',default=0)
    # Importo modelos avanzados de Manager
    objects = MedidorAguaLanzasMolino3Manager()
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'MedidorDeAguaLanzasMolino3'  # Nombre de Columna singular
      verbose_name_plural = 'MedidasDeAguaLanzasMolino3'  # Nombre en plural
    # Defino los titulos de las columnas del admin. de Django
    def __str__(self):
      return str(self.id) + ' - ' + str(self.created_at) + ' - ' + str(self.volumen)
