from rest_framework import serializers
from seguimiento.models import Seguimiento
from evaluacion.serializers import EvaluacionSerializer
from identificacion.serializers import IdentificacionSerializer
from aprobacion.serializers import AprobacionSerializer
from status.serializers import StatusSerializer


class SeguimientoSerializer(serializers.ModelSerializer):
    evaluacion = EvaluacionSerializer(source="evaluacion_id", read_only=True)
    identificacion = IdentificacionSerializer(source="identificacion_id", read_only=True)
    aprobacion = AprobacionSerializer(source="aprobacion_id", read_only=True)
    status = StatusSerializer(source="status_id", read_only=True)

    class Meta:
        model = Seguimiento
        fields = '__all__'