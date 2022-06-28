from rest_framework.routers import DefaultRouter
from maquina.views import MaquinaViewSet, MaquinasFallasDetails
from django.urls import path, include

maquina_route = DefaultRouter()

maquina_route.register(prefix='maquina', basename='maquina', viewset=MaquinaViewSet)

urlpatterns = [
    path('maquina_fallas_details/<int:id>',MaquinasFallasDetails.as_view(), name='maquina_fallas'),
]