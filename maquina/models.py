from django.db import models
from equipos.models import Equipo


# Create your models here.
class Maquina(models.Model):
    codigo = models.CharField(max_length=255, blank=True)
    machine_type = models.CharField(max_length=255, blank=True)
    descripcion = models.CharField(max_length=255, blank=True)
    funcion_equipo = models.CharField(max_length=255, blank=True)
    falla_funcion = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class EquipoMaquina(models.Model):
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    maquina_id = models.ForeignKey(Maquina, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)