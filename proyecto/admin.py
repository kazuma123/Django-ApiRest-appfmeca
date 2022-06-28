from django.contrib import admin
from proyecto.models import Proyecto, ProyectoEquiposFallas


# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'created_at']


# Register your models here.
@admin.register(ProyectoEquiposFallas)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ['proyecto','equipo', 'falla']