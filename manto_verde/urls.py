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

from falla.urls import fmeca_route
from equipo.urls import equipo_route
from proyecto.urls import proyecto_route
from equipos_completos.urls import equipos_completos_route
from maquina.urls import maquina_route
from especialidad.urls import especialidad_route
from estrategia.urls import estrategia_route
from tiempo.urls import tiempo_route
from tarea_secundaria.urls import tarea_secundaria_route

from aprobacion.urls import aprobacion_route
from clasificacion.urls import clasificacion_route
from evaluacion.urls import evaluacion_route
from identificacion.urls import identificacion_route
from origen.urls import origen_route
from seguimiento.urls import seguimiento_route
from status.urls import status_route

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

    path('api/', include(proyecto_route.urls)),
    path('api/', include(fmeca_route.urls)),
    path('api/', include(maquina_route.urls)),
    path('api/', include(equipo_route.urls)),
    #path('api/', include(equipos_completos_route.urls)),
    path('api/', include(especialidad_route.urls)),
    path('api/', include(estrategia_route.urls)),
    path('api/', include(tiempo_route.urls)),
    path('api/', include(tarea_secundaria_route.urls)),
    path('api/', include('maquina.urls')),
    path('api/', include('proyecto.urls')),
    #path('api/', include('falla.urls'))
    ####################################################
    path('api/', include(aprobacion_route.urls)),
    path('api/', include(clasificacion_route.urls)),
    path('api/', include(evaluacion_route.urls)),
    path('api/', include(identificacion_route.urls)),
    path('api/', include(origen_route.urls)),
    path('api/', include(seguimiento_route.urls)),
    path('api/', include(status_route.urls)),
]

