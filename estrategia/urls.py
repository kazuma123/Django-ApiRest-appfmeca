from rest_framework.routers import DefaultRouter
from estrategia.views import EstrategiaViewSet

estrategia_route = DefaultRouter()

estrategia_route.register(prefix='estrategia', basename='estrategia', viewset=EstrategiaViewSet)
