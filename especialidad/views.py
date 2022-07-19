from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from especialidad.serializers import EspecialidadSerializer
from especialidad.models import Especialidad
from falla.permission import IsAdminOrReadOnly
# Create your views here.


class EspecialidadViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()
