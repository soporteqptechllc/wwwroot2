# Import Django
from django.db import models

# Create your models.Manager here.
# ***********************************************************************************
class MedidorAguaRioManager(models.Manager):
    
    def medicion_by_id(self,id):
        return self.filter(
            id = id
        )

class MedidorAguaLanzasMolino3Manager(models.Manager):
    
    def medicion_by_id(self,id):
        return self.filter(
            id = id
        )