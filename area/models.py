from django.db import models
from proyecto.models import Proyecto

# Create your models here.
class Area(models.Model):
    proyecto = models.ManyToManyField(Proyecto)
    nombre = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

