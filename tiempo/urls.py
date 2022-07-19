from rest_framework.routers import DefaultRouter
from tiempo.views import TiempoViewSet


tiempo_route = DefaultRouter()

tiempo_route.register(prefix='tiempo', basename='tiempo', viewset=TiempoViewSet)