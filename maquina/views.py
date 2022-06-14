from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from maquina.serializers import MaquinaSerializer, EquipoMaquinaSerializer, MaquinaFmecaDetailsSerializer
from maquina.models import Maquina, EquipoMaquina
from rest_framework.views import APIView
from rest_framework.response import Response
from fmeca.models import FMeca

from fmeca.permission import IsAdminOrReadOnly
# Create your views here.


class MaquinaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = MaquinaSerializer
    queryset = Maquina.objects.all()


class EquipoMaquinaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = EquipoMaquinaSerializer
    queryset = EquipoMaquina.objects.all()


class MaquinasFallasDetails(APIView):
    def get(self, request, id=0):
        if id > 0:
            #queryset_fmeca = FMeca.objects.filter(equipo=id).all()
            queryset_machine = Maquina.objects.filter(id=id).all()
        else:
            queryset_fmeca = FMeca.objects.all()

        serializer_machine = MaquinaFmecaDetailsSerializer(queryset_machine, many=True)

        return Response(serializer_machine.data)