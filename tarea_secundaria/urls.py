from rest_framework.routers import DefaultRouter
from tarea_secundaria.views import TareaSecuandarioViewSet
from django.urls import path, include

tarea_secundaria_route = DefaultRouter()

tarea_secundaria_route.register(prefix='tarea_secundaria', basename='tarea_secundaria', viewset=TareaSecuandarioViewSet)