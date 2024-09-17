# Import REST FRAMEWORK
from rest_framework import serializers
# Register your local models here.
from .models import (
    MedidorAguaRio,
    MedidorAguaLanzasMolino3
    )

# Create your models.Serializer here.
# *******************************************************
# *******************************************************

class MedidorAguaRioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedidorAguaRio
        fields = ('__all__')

class MedidorAguaRioSerializer1(serializers.ModelSerializer):
    class Meta:
        model = MedidorAguaRio
        fields = (
            'datatime',
            'volumen',
            'flujo',
            'nivel',
            'bomba1',
            'bomba2'
        )
class MedidorAguaLanzasMolino3Serializer(serializers.ModelSerializer):
    class Meta:
        model = MedidorAguaLanzasMolino3
        fields = ('__all__')

class MedidorAguaLanzasMolino3Serializer1(serializers.ModelSerializer):
    class Meta:
        model = MedidorAguaLanzasMolino3
        fields = (
            'volumen',
        )