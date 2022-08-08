from rest_framework.routers import DefaultRouter
from identificacion.views import IdentificacionViewSet
from django.urls import path, include

identificacion_route = DefaultRouter()

identificacion_route.register(prefix='identificacion', basename='identificacion', viewset=IdentificacionViewSet)