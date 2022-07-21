from rest_framework import serializers
from falla.models import Falla
from maquina.serializerMaquina import MaquinaSpecificSerializer
from especialidad.serializers import EspecialidadSerializer
from estrategia.serializers import EstrategiaSerializer
from tiempo.serializers import TiempoSerializer


class FmecaSerializer(serializers.ModelSerializer):
    especialidad = EspecialidadSerializer(source='especialidad_id',read_only=True)
    medida_tiempo = TiempoSerializer(source='medida_tiempo_id',read_only=True)
    estrategia = EstrategiaSerializer(source='estrategia_id',read_only=True)
    medida_frecuencia = TiempoSerializer(source='medida_frecuencia_id',read_only=True)
    maquina = MaquinaSpecificSerializer(source='maquina_id', read_only=True)

    class Meta:
        model = Falla
        fields = "__all__"


# class AllFmecaSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Falla
#         fields = "__all__"

