from rest_framework.viewsets import ModelViewSet
from aprobacion.serializers import AprobacionSerializer
from aprobacion.models import Aprobacion
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class AprobacionViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = AprobacionSerializer
    queryset = Aprobacion.objects.all()
