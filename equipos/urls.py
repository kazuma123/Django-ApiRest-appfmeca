from rest_framework.routers import DefaultRouter
from equipos.views import EquipoViewSet, EquiposFallasDetails
from django.urls import path, include

equipo_route = DefaultRouter()

equipo_route.register(prefix='equipo', basename='equipo', viewset=EquipoViewSet)

urlpatterns = [
    path('equipos_details/<int:id>',EquiposFallasDetails.as_view(), name='equipos_fallas'),
]