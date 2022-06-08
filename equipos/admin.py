from django.contrib import admin
from equipos.models import Equipo, AreaEquipo


# Register your models here.
@admin.register(Equipo)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_areas','machine_type', 'descripcion', 'funcion', 'created_at']


@admin.register(AreaEquipo)
class AreaEquipoAdmin(admin.ModelAdmin):
    list_display = ['area_id','equipo_id', 'created_at', 'updated_at']
