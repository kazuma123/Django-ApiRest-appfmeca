from django.db import models
from area.models import Area

# Create your models here.
class Equipo(models.Model):
    area = models.ManyToManyField(Area, related_name="machine_list", through="AreaEquipo")
    machine_type = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    funcion = models.TextField()
    falla_funcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.machine_type

    def get_areas(self):
        return "\n".join([p.nombre for p in self.area.all()])


class AreaEquipo(models.Model):
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    equipo_id = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
