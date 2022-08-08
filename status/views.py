from rest_framework.viewsets import ModelViewSet
from status.serializers import StatusSerializer
from status.models import Status
from equipo.permission import IsAdminOrReadOnly
from rest_framework import permissions


class StatusViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
