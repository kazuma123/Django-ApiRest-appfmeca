from rest_framework.viewsets import ModelViewSet
from clasificacion.serializers import ClasificacionSerializer
from clasificacion.models import Clasificacion
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class ClasificacionViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ClasificacionSerializer
    queryset = Clasificacion.objects.all()
