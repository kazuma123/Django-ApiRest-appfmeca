from rest_framework import serializers
from proyecto.models import Proyecto
from area.serializers import AreaSerializer


class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'created_at']


class ProyectoAreaSerializer(serializers.ModelSerializer):
    proyecto_list = AreaSerializer(many=True, read_only=True)

    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'proyecto_list']