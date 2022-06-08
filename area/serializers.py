from rest_framework import serializers
from area.models import Area
from equipos.models import AreaEquipo

from equipos.serializers import EquiposSerializer

class AreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Area
        fields = ['id', 'nombre', 'created_at']


class AreaEquiposSerializer(serializers.ModelSerializer):
    machine_list = EquiposSerializer(many=True, read_only=True)
    area_list = AreaSerializer(many=True, read_only=True)
    class Meta:
        model = AreaEquipo
        fields = ['id','area_id', 'equipo_id','created_at', 'area_list','machine_list']