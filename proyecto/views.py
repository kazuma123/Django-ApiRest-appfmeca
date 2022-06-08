from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from proyecto.serializers import ProyectoSerializer, ProyectoAreaSerializer, ProyectoAreaModelSerializer
from proyecto.models import Proyecto
from area.models import ProyectoArea


class ProyectoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()


class ProyectoAreaSerializer(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProyectoAreaModelSerializer
    queryset = ProyectoArea.objects.all()