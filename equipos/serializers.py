from rest_framework import serializers
from equipos.models import Equipo
from fmeca.serializers import FmecaSerializer


class EquiposSerializer(serializers.ModelSerializer):
    fallas_equipo = FmecaSerializer(many=True, read_only=True)

    class Meta:
        model = Equipo
        fields = ['id', 'machine_type', 'descripcion', 'funcion', 'falla_funcion', 'created_at', 'area', 'fallas_equipo']