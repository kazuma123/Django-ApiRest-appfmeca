from django.db import models
from identificacion.models import Identificacion
from evaluacion.models import Evaluacion
from aprobacion.models import Aprobacion
from status.models import Status


# Create your models here.
class Seguimiento(models.Model):
    asignacion = models.CharField(max_length=255)
    fecha_asignacion = models.DateField()
    fecha_estimado_termino = models.DateField()
    overdue = models.IntegerField()
    avance = models.IntegerField()
    issues = models.CharField(max_length=255)
    asignado = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    evaluacion_id = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name="evaluacion_list_se", db_column="evaluacion_id", blank=True, null=True)
    identificacion_id = models.ForeignKey(Identificacion, on_delete=models.CASCADE, related_name="identificacion_list_se" ,db_column="identificacion_id")
    aprobacion_id = models.ForeignKey(Aprobacion, on_delete=models.CASCADE, related_name="aprobacion_list_se",db_column="aprobacion_id", blank=True, null=True)
    status_id = models.ForeignKey(Status, on_delete=models.CASCADE, related_name="status_list_se",db_column="status_id")

    def __str__(self):
        return self.asignacion

    class Meta:
        db_table = 'seguimiento'