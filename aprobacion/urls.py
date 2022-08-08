from rest_framework.routers import DefaultRouter
from aprobacion.views import AprobacionViewSet
from django.urls import path, include

aprobacion_route = DefaultRouter()

aprobacion_route.register(prefix='aprobacion', basename='aprobacion', viewset=AprobacionViewSet)
