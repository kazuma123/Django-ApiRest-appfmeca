from rest_framework.routers import DefaultRouter
from proyecto.views import ProyectoViewSet

proyecto_route = DefaultRouter()

proyecto_route.register(prefix='proyecto', basename='proyecto', viewset=ProyectoViewSet)