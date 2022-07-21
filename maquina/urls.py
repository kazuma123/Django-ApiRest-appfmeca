from rest_framework.routers import DefaultRouter
from maquina.views import MaquinaViewSet, MaquinasFallasDetails
from django.urls import path, include

maquina_route = DefaultRouter()

maquina_route.register(prefix='maquina', basename='maquina', viewset=MaquinaViewSet)

urlpatterns = [
    path('list_especific_getAllFallasMachine/<int:id>',MaquinasFallasDetails.as_view(), name='maquina_fallas'),
]