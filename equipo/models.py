from django.db import models


# Create your models here.
class Equipo(models.Model):
    tag = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre
