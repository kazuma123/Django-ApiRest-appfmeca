from rest_framework import serializers
from maquina.models import Maquina
from maquina.models import EquipoMaquina
from fmeca.serializers import FmecaSerializer
from fmeca.models import FMeca


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'


class EquipoMaquinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipoMaquina
        fields = '__all__'


class MaquinaFmecaDetailsSerializer(serializers.ModelSerializer):
    fmeca_list = FmecaSerializer(many=True, read_only=True)

    class Meta:
        model = Maquina
        fields = '__all__'