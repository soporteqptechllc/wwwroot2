# Import REST FRAMEWORK
from rest_framework import serializers
# Local
from .models import (
    ReporteLAB, 
 
    )

# Serializador de MaestroDeMateriales
class ReporteLABSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReporteLAB
        fields = ('__all__')