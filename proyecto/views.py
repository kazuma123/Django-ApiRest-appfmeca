from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from proyecto.serializers import ProyectoSerializer, ProyectoEquiposFallasSerializer, ProyectoEquiposFallasDetailsSerializer, ProyectoEquiposSerializer
from proyecto.models import Proyecto, ProyectoEquiposFallas
from rest_framework.views import APIView
from rest_framework.response import Response


class ProyectoViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()


class ProyectoEquiposFallasViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = ProyectoEquiposFallasDetailsSerializer
    queryset = ProyectoEquiposFallas.objects.all()


class ProyectoEquiposFallasDetailsApiView(APIView):
    def get(self, request, id=0):
        if id > 0:
            queryset_machine = ProyectoEquiposFallas.objects.filter(proyecto_id=id)

        serializer_machine = ProyectoEquiposFallasDetailsSerializer(queryset_machine, many=True)
        return Response(serializer_machine.data)


class ProyectoEquiposDetailsApiView(APIView):
    def get(self, request, id=0):
        if id > 0:
            queryset_machine = Proyecto.objects.filter(id=id)

        serializer_machine = ProyectoEquiposSerializer(queryset_machine, many=True)
        return Response(serializer_machine.data)