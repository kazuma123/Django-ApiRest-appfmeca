from rest_framework.routers import DefaultRouter
from clasificacion.views import ClasificacionViewSet
from django.urls import path, include

clasificacion_route = DefaultRouter()

clasificacion_route.register(prefix='clasificacion', basename='clasificacion', viewset=ClasificacionViewSet)