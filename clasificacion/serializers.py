from rest_framework import serializers
from clasificacion.models import Clasificacion


class ClasificacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clasificacion
        fields = '__all__'