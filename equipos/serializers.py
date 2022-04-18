from rest_framework import serializers
from equipos.models import Equipo


class EquiposSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipo
        fields = ['id', 'machine_type', 'descripcion', 'funcion', 'falla_funcion', 'created_at', 'area']