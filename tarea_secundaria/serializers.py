from rest_framework import serializers
from tarea_secundaria.models import TareaSecundaria
from tiempo.serializers import TiempoSerializer
from falla.serializers import FmecaSerializer


class TareaSecuandariaSerializer(serializers.ModelSerializer):
    tiempo = TiempoSerializer(source="medida_tiempo_id", read_only=True)
    fallas = FmecaSerializer(source="falla_id", read_only=True)

    class Meta:
        model = TareaSecundaria
        fields = '__all__'
