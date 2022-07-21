from rest_framework import serializers
from maquina.models import Maquina


class MaquinaSpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'