from rest_framework.routers import DefaultRouter
from fmeca.views import FmecaViewSet

fmeca_route = DefaultRouter()

fmeca_route.register(prefix='fmeca', basename='fmeca', viewset=FmecaViewSet)
# fmeca_route.register(prefix='maquina_fmeca', basename='maquina_fmeca', viewset=MaquinaFmecaViewSet)