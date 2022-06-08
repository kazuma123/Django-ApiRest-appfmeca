from django.contrib import admin
from equipos.models import Equipo, AreaEquipo


# Register your models here.
@admin.register(Equipo)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_areas','machine_type', 'descripcion', 'funcion', 'created_at']


admin.site.register(AreaEquipo)