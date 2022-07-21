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
    proyecto = ProyectoSerializer(source="proyecto_id", read_only=True)
    equipo = EquiposOnlySerializer(source="equipo_id", read_only=True)
    falla = FmecaSerializer(source="falla_id", read_only=True)

    class Meta:
        model = ProyectoEquiposFallas
        fields = '__all__'


class ProyectoEquiposSerializer(serializers.ModelSerializer):
    equipos_list = EquiposOnlySerializer(many=True, read_only=True)

    class Meta:
        model = Proyecto
        fields = '__all__'