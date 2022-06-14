from rest_framework import serializers
from equipos.models import Equipo
from fmeca.models import MaquinaFmeca
from fmeca.serializers import FmecaSerializer


class EquiposSerializer(serializers.ModelSerializer):
    fallas_equipo = FmecaSerializer(many=True, read_only=True)

    class Meta:
        model = Equipo
        fields = '__all__'


class EquipoFmecaSerializer(serializers.ModelSerializer):
    #fallas_equipo = FmecaSerializer(many=True, read_only=True)
    #equipo_list = EquiposSerializer(many=True, read_only=True)

    class Meta:
        model = MaquinaFmeca
        fields ='__all__'