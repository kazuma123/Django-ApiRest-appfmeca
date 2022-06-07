from django.db import models
from proyecto.models import Proyecto

# Create your models here.
class Area(models.Model):
    proyecto = models.ManyToManyField(Proyecto, related_name="proyecto_list")
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

    def get_proyects(self):
        return "\n".join([p.nombre for p in self.proyecto.all()])

