from django.db import models


# Create your models here.
class EquiposCompletos(models.Model):

    #area = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    machine_type = models.CharField(max_length=255)
    descripcion = models.TextField()
    funcion_equipo = models.TextField()
    falla_funcional = models.TextField()
    ds_modo_falla = models.CharField(max_length=255)
    ds_efecto_modo_falla = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine_type

    class Meta:
        db_table = 'equipo_completos'

