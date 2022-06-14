from rest_framework import serializers
from maquina.models import Maquina
from maquina.models import EquipoMaquina


class MaquinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Maquina
        fields = '__all__'


class EquipoMaquinaSerializer(serializers.ModelSerializer):

    class Meta:
        model = EquipoMaquina
        fields = '__all__'

