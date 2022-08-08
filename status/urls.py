from rest_framework.routers import DefaultRouter
from status.views import StatusViewSet
from django.urls import path, include

status_route = DefaultRouter()

status_route.register(prefix='status', basename='status', viewset=StatusViewSet)