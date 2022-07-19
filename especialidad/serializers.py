from rest_framework import serializers
from especialidad.models import Especialidad


class EspecialidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Especialidad
        fields = '__all__'
