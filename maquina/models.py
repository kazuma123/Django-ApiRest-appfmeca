from django.db import models
from equipo.models import Equipo


# Create your models here.
class Maquina(models.Model):
    codigo = models.CharField(max_length=255, blank=True)
    machine_type = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    funcion_equipo = models.CharField(max_length=255, blank=True)
    falla_funcion = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
