from django.db import models
from evaluacion.models import Evaluacion


# Create your models here.
class Aprobacion(models.Model):
    aprobador = models.CharField(max_length=255)
    fecha_aprobacion = models.DateField()
    asignado = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    evaluacion_id = models.ForeignKey(Evaluacion, on_delete=models.CASCADE, related_name="evaluacion_list_apro", db_column="evaluacion_id")

    def __str__(self):
        return self.aprobador

    class Meta:
        db_table = 'aprobacion'