from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from estrategia.serializers import EstrategiaSerializer
from estrategia.models import Estrategia
from falla.permission import IsAdminOrReadOnly
# Create your views here.


class EstrategiaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EstrategiaSerializer
    queryset = Estrategia.objects.all()
