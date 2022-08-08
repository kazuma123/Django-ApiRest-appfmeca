from rest_framework.viewsets import ModelViewSet
from identificacion.serializers import IdentificacionSerializer
from identificacion.models import Identificacion
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class IdentificacionViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = IdentificacionSerializer
    queryset = Identificacion.objects.all()
