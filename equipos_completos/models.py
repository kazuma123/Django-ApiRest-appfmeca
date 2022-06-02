from django.db import models


# Create your models here.
class EquiposCompletos(models.Model):
    machine_type = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    tag_equipo = models.CharField(max_length=255)
    equipo_principal = models.CharField(max_length=255)
    sistema = models.CharField(max_length=255)
    sub_sistema = models.CharField(max_length=255)
    lazo_control = models.CharField(max_length=255)
    tag_componente = models.CharField(max_length=255)
    componente = models.CharField(max_length=255)
    ubicacion_tecnica = models.CharField(max_length=255)
    numero_equipo = models.CharField(max_length=255)
    descripcion_equipo = models.TextField()
    criticidad = models.CharField(max_length=255)
    funcion_equipo = models.TextField()
    falla_funcional = models.TextField()
    componente_pauta = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine_type
