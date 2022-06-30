from rest_framework import serializers
from proyecto.models import Proyecto
from proyecto.models import ProyectoEquiposFallas
from equipo.serializers import EquiposSerializer, EquiposOnlySerializer
from falla.serializers import FmecaSerializer


class ProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = '__all__'


class ProyectoEquiposFallasSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProyectoEquiposFallas
        fields = '__all__'


class PruebaSerializer(serializers.ModelSerializer):
    proyecto = EquiposSerializer(read_only=True)

    class Meta:
        model = ProyectoEquiposFallas
        fields = '__all__'


class ProyectoEquiposFallasDetailsSerializer(serializers.ModelSerializer):
    proyecto_id = ProyectoSerializer(read_only=True)
    equipo_id = EquiposOnlySerializer(read_only=True)
    falla_id = FmecaSerializer(read_only=True)

    class Meta:
        model = ProyectoEquiposFallas
        fields = '__all__'
