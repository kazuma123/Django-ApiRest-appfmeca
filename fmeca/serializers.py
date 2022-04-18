from rest_framework import serializers
from fmeca.models import FMeca


class FmecaSerializer(serializers.ModelSerializer):

    class Meta:
        model = FMeca
        fields = ['id', 'ds_modo_falla', 'ds_efecto_falla', 'descripcion_tarea', 'created_at', 'equipo']