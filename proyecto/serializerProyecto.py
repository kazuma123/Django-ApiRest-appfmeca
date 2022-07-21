from rest_framework import serializers
from proyecto.models import Proyecto


class OtherProyectoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Proyecto
        fields = '__all__'