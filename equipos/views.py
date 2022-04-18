from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from equipos.serializers import EquiposSerializer
from equipos.models import Equipo
from equipos.permission import IsAdminOrReadOnly
# Create your views here.


class EquipoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EquiposSerializer
    queryset = Equipo.objects.all()
