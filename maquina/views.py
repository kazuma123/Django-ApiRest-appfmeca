from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from maquina.serializers import MaquinaSerializer, MaquinaFmecaDetailsSerializer
from maquina.models import Maquina
from rest_framework.views import APIView
from rest_framework.response import Response
from falla.models import Falla

from falla.permission import IsAdminOrReadOnly
# Create your views here.


class MaquinaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = MaquinaSerializer
    queryset = Maquina.objects.all()


class MaquinasFallasDetails(APIView):
    def get(self, request, id=0):
        if id > 0:

            queryset_machine = Maquina.objects.filter(id=id).all()
        else:
            queryset_fmeca = Falla.objects.all()

        serializer_machine = MaquinaFmecaDetailsSerializer(queryset_machine, many=True)

        return Response(serializer_machine.data)