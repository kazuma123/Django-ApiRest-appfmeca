from rest_framework.routers import DefaultRouter
from proyecto.views import ProyectoViewSet, ProyectoEquiposFallasViewSet, ProyectoEquiposFallasDetailsApiView, ProyectoEquiposDetailsApiView
from django.urls import path, include

proyecto_route = DefaultRouter()

proyecto_route.register(prefix='proyecto', basename='proyecto', viewset=ProyectoViewSet)
proyecto_route.register(prefix='proyecto_equipo', basename='proyecto_equipo', viewset=ProyectoEquiposFallasViewSet)

urlpatterns = [
    path('list_especific_getAllProyectoEquipoFallas_ProyectoEspecifico/<int:id>', ProyectoEquiposFallasDetailsApiView.as_view(), name='proyecto_equipo_fallas'),
    path('list_especific_getAllEquiposProyectos/<int:id>', ProyectoEquiposDetailsApiView.as_view(), name='list_especific_getAllEquiposProyectos'),
]