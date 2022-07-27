from django.db import models
from tiempo.models import Tiempo
from falla.models import Falla


# Create your models here.
class TareaSecundaria(models.Model):
    medida_tiempo_id = models.OneToOneField(Tiempo, on_delete=models.CASCADE, related_name="tarea_tiempo_list", db_column='medida_tiempo_id')
    falla_id = models.ForeignKey(Falla, on_delete=models.CASCADE, related_name="tarea_falla_list", db_column='falla_id')
    descripcion_accion_secundaria = models.CharField(max_length=255)
    duracion_trabajo = models.IntegerField()
    personas = models.IntegerField()
    repuesto = models.CharField(max_length=255)
    descripcion_repuesto = models.CharField(max_length=255)
    procedimiento_trabajo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion_accion_secundaria

    class Meta:
        db_table = 'tarea_secundario'
