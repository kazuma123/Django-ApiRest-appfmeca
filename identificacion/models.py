from django.db import models
from origen.models import Origen
from clasificacion.models import Clasificacion


# Create your models here.
class Identificacion(models.Model):
    fecha_ingreso = models.DateField()
    originador = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    tag_descripcion = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    origen_id = models.ForeignKey(Origen, on_delete=models.CASCADE, related_name="origen_list_ide", db_column="origen_id")
    clasificacion_id = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name="clasificacion_list_ide", db_column="clasificacion_id")

    def __str__(self):
        return self.originador

    class Meta:
        db_table = 'identificacion'