from rest_framework import serializers
from proyecto.models import Proyecto
from area.serializers import AreaSerializer
from area.models import ProyectoArea


class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'created_at']


class ProyectoAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProyectoArea
        fields = ['id','proyecto_id']


# class ProyectoAreaModelSerializer(serializers.ModelSerializer):
#     area_list = AreaSerializer(many=True, read_only=True)
#     proyecto_area = ProyectoAreaSerializer(source="proyectoarea_set", many=True)
#
#     class Meta:
#         model = Proyecto
#         fields = ['id','nombre','descripcion','area_list','proyecto_area']

class ProyectoAreaModelSerializer(serializers.ModelSerializer):
    #proyecto = ProyectoSerializer(read_only=True)
    #proyecto_area = ProyectoAreaSerializer(source="proyectoarea_set", many=True)
    #proyecto_area = ProyectoSerializer(source="proyecto_set", many=True)

    class Meta:
        model = ProyectoArea
        fields = '__all__'