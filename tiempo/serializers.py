from rest_framework import serializers
from tiempo.models import Tiempo


class TiempoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tiempo
        fields = '__all__'
