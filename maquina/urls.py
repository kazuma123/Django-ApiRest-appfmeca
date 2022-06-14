from rest_framework.routers import DefaultRouter
from maquina.views import MaquinaViewSet, EquipoMaquinaViewSet, MaquinasFallasDetails
from django.urls import path, include

maquina_route = DefaultRouter()

maquina_route.register(prefix='maquina', basename='maquina', viewset=MaquinaViewSet)
maquina_route.register(prefix='equipo_maquina', basename='equipo_maquina', viewset=EquipoMaquinaViewSet)

urlpatterns = [
    path('maquina_fallas_details/<int:id>',MaquinasFallasDetails.as_view(), name='maquina_fallas'),
]