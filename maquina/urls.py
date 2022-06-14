from rest_framework.routers import DefaultRouter
from maquina.views import MaquinaViewSet, EquipoMaquinaViewSet

maquina_route = DefaultRouter()

maquina_route.register(prefix='maquina', basename='maquina', viewset=MaquinaViewSet)
maquina_route.register(prefix='equipo_maquina', basename='equipo_maquina', viewset=EquipoMaquinaViewSet)