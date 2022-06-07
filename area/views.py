from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from area.serializers import AreaSerializer, AreaEquiposSerializer
from equipos.serializers import EquiposSerializer
from area.models import Area
from equipos.models import Equipo
from equipos.permission import IsAdminOrReadOnly
# Create your views here.


class AreaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = AreaSerializer
    queryset = Area.objects.all()

class AreaEquiposViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = AreaEquiposSerializer
    queryset = Area.objects.all()