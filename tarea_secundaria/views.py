from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from tarea_secundaria.serializers import TareaSecuandariaSerializer
from tarea_secundaria.models import TareaSecundaria
from rest_framework.views import APIView
from rest_framework.response import Response
from falla.permission import IsAdminOrReadOnly
# Create your views here.


class TareaSecuandarioViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = TareaSecuandariaSerializer
    queryset = TareaSecundaria.objects.all()


# class AllFmecaDetailsViewSet(APIView):
#     #permission_classes = [IsAdminOrReadOnly]
#     def get(self, request):
#         items = Falla.objects.all()
#         serializer = AllFmecaSerializer(items, many=True)
#         return Response(serializer.data)
