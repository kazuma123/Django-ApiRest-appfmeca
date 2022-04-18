from rest_framework.routers import DefaultRouter
from equipos.views import EquipoViewSet

equipo_route = DefaultRouter()

equipo_route.register(prefix='equipo', basename='equipo', viewset=EquipoViewSet)
