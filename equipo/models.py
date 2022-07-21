from django.db import models


# Create your models here.
class Equipo(models.Model):
    proyecto_id = models.ForeignKey("proyecto.Proyecto", on_delete=models.CASCADE, related_name="equipos_list", db_column="proyecto_id")
    tag = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField()
    funcion = models.CharField(max_length=255, blank=True)
    criticidad = models.IntegerField()
    ubicacion_tecnica = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'equipo'
