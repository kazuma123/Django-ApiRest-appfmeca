from rest_framework.routers import DefaultRouter
from origen.views import OrigenViewSet
from django.urls import path, include

origen_route = DefaultRouter()

origen_route.register(prefix='origen', basename='origen', viewset=OrigenViewSet)