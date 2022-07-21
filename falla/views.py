from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from falla.serializers import FmecaSerializer
from falla.models import Falla
from rest_framework.views import APIView
from rest_framework.response import Response
from falla.permission import IsAdminOrReadOnly
# Create your views here.


class FmecaViewSet(ModelViewSet):
    #permission_classes = [IsAdminOrReadOnly]
    serializer_class = FmecaSerializer
    queryset = Falla.objects.all()


# class AllFmecaDetailsViewSet(APIView):
#     #permission_classes = [IsAdminOrReadOnly]
#     def get(self, request):
#         items = Falla.objects.all()
#         serializer = AllFmecaSerializer(items, many=True)
#         return Response(serializer.data)



# class MaquinaFmecaViewSet(ModelViewSet):
#     #permission_classes = [IsAdminOrReadOnly]
#     serializer_class = MaquinaFmecaSerializer
#     queryset = MaquinaFmeca.objects.all()