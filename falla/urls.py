from rest_framework.routers import DefaultRouter
from falla.views import FmecaViewSet
from django.urls import path, include

fmeca_route = DefaultRouter()

fmeca_route.register(prefix='falla', basename='falla', viewset=FmecaViewSet)

