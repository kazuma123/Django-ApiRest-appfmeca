from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from fmeca.serializers import FmecaSerializer, MaquinaFmecaSerializer
from fmeca.models import FMeca, MaquinaFmeca
from fmeca.permission import IsAdminOrReadOnly
# Create your views here.


class FmecaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = FmecaSerializer
    queryset = FMeca.objects.all()


class MaquinaFmecaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = MaquinaFmecaSerializer
    queryset = MaquinaFmeca.objects.all()