from django.contrib import admin
from maquina.models import Maquina


# Register your models here.
@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ['codigo','machine_type', 'descripcion','funcion_equipo','falla_funcion','created_at','updated_at']

