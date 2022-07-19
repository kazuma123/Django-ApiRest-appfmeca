from rest_framework import serializers
from estrategia.models import Estrategia


class EstrategiaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estrategia
        fields = '__all__'

