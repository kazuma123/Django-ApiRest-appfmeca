from django.db import models
from falla.models import Falla
from equipo.models import Equipo


# Create your models here.
class Proyecto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class ProyectoEquiposFallas(models.Model):
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    falla_id = models.ForeignKey(Falla, on_delete=models.CASCADE)