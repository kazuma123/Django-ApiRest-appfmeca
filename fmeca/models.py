from django.db import models
from equipos.models import Equipo


# Create your models here.
class FMeca(models.Model):
    equipo = models.ForeignKey(Equipo, related_name='fallas_equipo', on_delete=models.CASCADE)
    ds_modo_falla = models.CharField(max_length=255)
    ds_efecto_falla = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ds_efecto_falla