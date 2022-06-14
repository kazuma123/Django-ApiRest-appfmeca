from django.contrib import admin
from maquina.models import Maquina, EquipoMaquina


# Register your models here.
@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ['codigo','machine_type', 'descripcion','funcion_equipo','falla_funcion','created_at','updated_at']


@admin.register(EquipoMaquina)
class EquipoMaquinaAdmin(admin.ModelAdmin):
    list_display = ['equipo_id','maquina_id', 'created_at','updated_at']