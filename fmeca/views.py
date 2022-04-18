from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from fmeca.serializers import FmecaSerializer
from fmeca.models import FMeca
from fmeca.permission import IsAdminOrReadOnly
# Create your views here.


class FmecaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = FmecaSerializer
    queryset = FMeca.objects.all()
