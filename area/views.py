from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from area.serializers import AreaSerializer
from area.models import Area
from equipos.permission import IsAdminOrReadOnly
# Create your views here.


class AreaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = AreaSerializer
    queryset = Area.objects.all()
