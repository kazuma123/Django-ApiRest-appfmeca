from rest_framework import serializers
from area.models import Area
from equipos.models import Equipo
from equipos.serializers import EquiposSerializer

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ['id', 'nombre', 'created_at']


class AreaEquiposSerializer(serializers.ModelSerializer):
    machine_list = EquiposSerializer(many=True, read_only=True)

    class Meta:
        model = Area
        fields = ['id', 'nombre', 'machine_list']