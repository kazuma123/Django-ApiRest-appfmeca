from django.db import models
from maquina.models import Maquina


# Create your models here.
class Falla(models.Model):
    maquina_id = models.ForeignKey(Maquina, on_delete=models.CASCADE, related_name="falla_list")
    ds_modo_falla = models.CharField(max_length=255)
    ds_efecto_modo_falla = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ds_efecto_modo_falla


# class MaquinaFmeca(models.Model):
#     maquina_id = models.ForeignKey(Maquina, on_delete=models.CASCADE)
#     fmeca_id = models.ForeignKey(FMeca, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
