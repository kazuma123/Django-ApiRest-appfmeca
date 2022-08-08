from rest_framework.routers import DefaultRouter
from seguimiento.views import SeguimientoViewSet
from django.urls import path, include

seguimiento_route = DefaultRouter()

seguimiento_route.register(prefix='seguimiento', basename='seguimiento', viewset=SeguimientoViewSet)