from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tiempo.serializers import TiempoSerializer
from tiempo.models import Tiempo


class TiempoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = TiempoSerializer
    queryset = Tiempo.objects.all()
