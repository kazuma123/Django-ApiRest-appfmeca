from rest_framework.viewsets import ModelViewSet
from evaluacion.serializers import EvaluacionSerializer
from evaluacion.models import Evaluacion
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class EvaluacionViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EvaluacionSerializer
    queryset = Evaluacion.objects.all()
