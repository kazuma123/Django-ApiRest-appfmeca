from django.db import models
from area.models import Area


# Create your models here.
class Equipo(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    machine_type = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    funcion = models.TextField()
    falla_funcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine_type
