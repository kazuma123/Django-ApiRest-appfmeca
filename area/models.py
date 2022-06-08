from django.db import models
from proyecto.models import Proyecto


# Create your models here.
class Area(models.Model):
    proyecto = models.ManyToManyField(Proyecto, related_name="area_list", through="ProyectoArea")
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_proyects(self):
        return "\n".join([p.nombre for p in self.proyecto.all()])


class ProyectoArea(models.Model):
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)