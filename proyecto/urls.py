from rest_framework.routers import DefaultRouter
from proyecto.views import ProyectoViewSet, ProyectoEquiposFallasViewSet, ProyectoEquiposFallasDetailsApiView
from django.urls import path, include

proyecto_route = DefaultRouter()

proyecto_route.register(prefix='proyecto', basename='proyecto', viewset=ProyectoViewSet)
proyecto_route.register(prefix='proyecto_equipo', basename='proyecto_equipo', viewset=ProyectoEquiposFallasViewSet)

urlpatterns = [
    path('proyecto_equipo_fallas/<int:id>', ProyectoEquiposFallasDetailsApiView.as_view(), name='proyecto_equipo_fallas'),
]