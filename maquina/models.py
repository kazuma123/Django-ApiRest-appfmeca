from django.db import models
from equipo.models import Equipo


# Create your models here.
class Maquina(models.Model):
    codigo = models.CharField(max_length=255)
    machine_type = models.CharField(max_length=255)
    description_machine_type = models.CharField(max_length=255)
    funcion = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine_type

    class Meta:
        db_table = 'maquina'