from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from falla.serializers import FmecaSerializer
from falla.models import Falla
from falla.permission import IsAdminOrReadOnly
# Create your views here.


class FmecaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = FmecaSerializer
    queryset = Falla.objects.all()


# class MaquinaFmecaViewSet(ModelViewSet):
#     #permission_classes = [IsAdminOrReadOnly]
#     serializer_class = MaquinaFmecaSerializer
#     queryset = MaquinaFmeca.objects.all()