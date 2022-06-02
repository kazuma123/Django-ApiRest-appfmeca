from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from proyecto.serializers import ProyectoSerializer
from proyecto.models import Proyecto


class ProyectoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()