from django.db import models


# Create your models here.
class Especialidad(models.Model):
    siglas = models.CharField(max_length=255)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)