from rest_framework.viewsets import ModelViewSet
from origen.serializers import OrigenSerializer
from origen.models import Origen
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class OrigenViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = OrigenSerializer
    queryset = Origen.objects.all()
