from rest_framework import serializers
from maquina.models import Maquina
from falla.serializers import FmecaSerializer
from falla.models import Falla


class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'


class MaquinaFmecaDetailsSerializer(serializers.ModelSerializer):
    falla_list = FmecaSerializer(many=True, read_only=True)

    class Meta:
        model = Maquina
        fields = '__all__'