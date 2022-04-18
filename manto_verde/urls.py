"""manto_verde URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from fmeca.urls import fmeca_route
from equipos.urls import equipo_route
from area.urls import area_route
schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Documentacion de la API blog",
      terms_of_service="",
      contact=openapi.Contact(email="echambir@unsa.edu.pe"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   #permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout = 0), name = 'schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout = 0), name = 'schema-redoc'),
    path('api/', include('users.urls')),

    path('api/', include(fmeca_route.urls)),
    path('api/', include(equipo_route.urls)),
    path('api/', include(area_route.urls))
]

