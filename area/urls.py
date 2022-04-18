from rest_framework.routers import DefaultRouter
from area.views import AreaViewSet

area_route = DefaultRouter()

area_route.register(prefix='area', basename='area', viewset=AreaViewSet)