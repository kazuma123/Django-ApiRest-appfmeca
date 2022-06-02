from rest_framework import serializers
from equipos_completos.models import EquiposCompletos

class EquiposCompletosSerializers(serializers.ModelSerializer):
    class Meta:
        model = EquiposCompletos
        fields = '__all__'