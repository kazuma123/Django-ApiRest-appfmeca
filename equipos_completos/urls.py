from rest_framework.routers import DefaultRouter
from equipos_completos.views import EquiposCompletosViewSet

equipos_completos_route = DefaultRouter()

equipos_completos_route.register(prefix='equipos_completos_route', basename='equipos_completos_route', viewset=EquiposCompletosViewSet)
