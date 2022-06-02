from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from equipos_completos.serializers import EquiposCompletosSerializers
from equipos_completos.models import EquiposCompletos
from fmeca.permission import IsAdminOrReadOnly
# Create your views here.


class EquiposCompletosViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EquiposCompletosSerializers
    queryset = EquiposCompletos.objects.all()
