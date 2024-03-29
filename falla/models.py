from django.db import models
from maquina.models import Maquina
from estrategia.models import Estrategia
from especialidad.models import Especialidad
from tiempo.models import Tiempo


# Create your models here.
class Falla(models.Model):
    maquina_id = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name="falla_list", db_column='maquina_id')
    especialidad_id = models.ForeignKey(Especialidad, on_delete=models.CASCADE, related_name="especialidad_list", db_column='especialidad_id')
    medida_tiempo_id = models.ForeignKey(Tiempo, on_delete=models.CASCADE, related_name="tiempo_list", db_column='medida_tiempo_id')
    estrategia_id = models.ForeignKey(Estrategia, on_delete=models.CASCADE, related_name="estrategia_list", db_column='estrategia_id')
    medida_frecuencia_id = models.ForeignKey(Tiempo, on_delete=models.CASCADE, related_name="medida_list", db_column='medida_frecuencia_id')
    falla_funcional = models.CharField(max_length=255)
    modo_falla = models.CharField(max_length=255)
    causas = models.CharField(max_length=255)
    efecto_modo_falla = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()
    parametros = models.CharField(max_length=255)
    repuesto = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    tiempo = models.IntegerField()
    personas = models.IntegerField()
    frecuencia = models.IntegerField()
    procedimiento_seguridad = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.efecto_modo_falla

    class Meta:
        db_table = 'falla_tarea'


# class MaquinaFmeca(models.Model):
#     maquina_id = models.ForeignKey(Maquina, on_delete=models.CASCADE)
#     fmeca_id = models.ForeignKey(FMeca, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
