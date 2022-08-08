from rest_framework import serializers
from aprobacion.models import Aprobacion
from evaluacion.serializers import EvaluacionSerializer


class AprobacionSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer(source="evaluacion_id", read_only=True)

    class Meta:
        model = Aprobacion
        fields = '__all__'