from rest_framework.viewsets import ModelViewSet
from seguimiento.serializers import SeguimientoSerializer
from seguimiento.models import Seguimiento
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class SeguimientoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = SeguimientoSerializer
    queryset = Seguimiento.objects.all()
