from rest_framework.routers import DefaultRouter
from area.views import AreaViewSet, AreaEquiposViewSet

area_route = DefaultRouter()

area_route.register(prefix='area', basename='area', viewset=AreaViewSet)
area_route.register(prefix='area_equipo', basename='area_equipo', viewset=AreaEquiposViewSet)