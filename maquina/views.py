from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from maquina.serializers import MaquinaSerializer, EquipoMaquinaSerializer
from maquina.models import Maquina, EquipoMaquina
from fmeca.permission import IsAdminOrReadOnly
# Create your views here.


class MaquinaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = MaquinaSerializer
    queryset = Maquina.objects.all()


class EquipoMaquinaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EquipoMaquinaSerializer
    queryset = EquipoMaquina.objects.all()