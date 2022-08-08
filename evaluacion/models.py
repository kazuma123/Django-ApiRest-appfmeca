from django.db import models
from identificacion.models import Identificacion
from clasificacion.models import Clasificacion
from status.models import Status


# Create your models here.
class Evaluacion(models.Model):
    impacto = models.CharField(max_length=255)
    solucion_propuesta = models.CharField(max_length=255)
    riesgo = models.IntegerField()
    nivel_esfuerzo = models.IntegerField()
    nivel_beneficio = models.IntegerField()
    fecha_espera_solucion = models.DateField()
    alcance = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    identificacion_id = models.ForeignKey(Identificacion, on_delete=models.CASCADE, related_name="identificacion_list_ev", db_column="identificacion_id")
    clasificacion_id = models.ForeignKey(Clasificacion, on_delete=models.CASCADE, related_name="clasificacion_list_ev", db_column="clasificacion_id")
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status_list_ev", db_column="status_id")


    def __str__(self):
        return self.impacto

    class Meta:
        db_table = 'evaluacion'