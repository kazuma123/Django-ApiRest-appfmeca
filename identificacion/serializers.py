from rest_framework import serializers
from identificacion.models import Identificacion
from origen.serializers import OrigenSerializer
from clasificacion.serializers import ClasificacionSerializer


class IdentificacionSerializer(serializers.ModelSerializer):
    origen = OrigenSerializer(source="origen_id", read_only=True)
    clasificacion = ClasificacionSerializer(source="clasificacion_id", read_only=True)

    class Meta:
        model = Identificacion
        fields = '__all__'