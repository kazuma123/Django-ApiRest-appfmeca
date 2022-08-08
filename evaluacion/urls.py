from rest_framework.routers import DefaultRouter
from evaluacion.views import EvaluacionViewSet
from django.urls import path, include

evaluacion_route = DefaultRouter()

evaluacion_route.register(prefix='evaluacion', basename='evaluacion', viewset=EvaluacionViewSet)