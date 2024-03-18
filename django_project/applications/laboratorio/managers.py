# Import Django
from django.db import models

# models avanzados
class ReporteLABManager(models.Manager):

    def reporte_by_datetime(self,fecha):
        return self.filter(
            datetime__gte = fecha
        )
    # Estos 2 metodos son iguales en el resultado
    def reporte_range_datetime_1(self,fecha1,fecha2):
        return self.filter(
            datetime__range = (fecha1,fecha2)
            ).order_by('id')
    def reporte_range_datetime_2(self,fecha1,fecha2):
        return self.filter(datetime__gte = fecha1).filter(datetime__lte = fecha2)