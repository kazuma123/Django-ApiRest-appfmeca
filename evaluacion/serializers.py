from rest_framework import serializers
from evaluacion.models import Evaluacion
from identificacion.serializers import IdentificacionSerializer
from clasificacion.serializers import ClasificacionSerializer
from status.serializers import StatusSerializer


class EvaluacionSerializer(serializers.ModelSerializer):
    identificacion = IdentificacionSerializer(source="identificacion_id", read_only=True)
    clasificacion = ClasificacionSerializer(source="clasificacion_id", read_only=True)
    status = StatusSerializer(source="status_id", read_only=True)

    class Meta:
        model = Evaluacion
        fields = '__all__'