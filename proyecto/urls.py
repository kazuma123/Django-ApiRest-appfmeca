from rest_framework.routers import DefaultRouter
from proyecto.views import ProyectoViewSet, ProyectoAreaSerializer

proyecto_route = DefaultRouter()

proyecto_route.register(prefix='proyecto', basename='proyecto', viewset=ProyectoViewSet)
proyecto_route.register(prefix='proyecto_area', basename='proyecto_area', viewset=ProyectoAreaSerializer)