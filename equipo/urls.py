from rest_framework.routers import DefaultRouter
from equipo.views import EquipoViewSet
from django.urls import path, include

equipo_route = DefaultRouter()

equipo_route.register(prefix='equipo', basename='equipo', viewset=EquipoViewSet)
#equipo_route.register(prefix='equipo_fallas', basename='equipo_fallas', viewset=MaquinaFmecaViewSet)
