from rest_framework.routers import DefaultRouter
from especialidad.views import EspecialidadViewSet

especialidad_route = DefaultRouter()

especialidad_route.register(prefix='especialidad', basename='especialidad', viewset=EspecialidadViewSet)
