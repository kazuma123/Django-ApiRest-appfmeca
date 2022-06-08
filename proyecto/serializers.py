from rest_framework import serializers
from proyecto.models import Proyecto
from area.serializers import AreaSerializer
from area.models import ProyectoArea

class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'created_at']


class ProyectoAreaSerializer(serializers.ModelSerializer):
    area_list = AreaSerializer(many=True, read_only=True)
    proyecto_list = ProyectoSerializer(many=True, read_only=True)

    class Meta:
        model = ProyectoArea
        fields = ['id','proyecto_id', 'area_id','created_at','area_list','proyecto_list']