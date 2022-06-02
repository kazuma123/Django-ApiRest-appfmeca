from django.contrib import admin
from proyecto.models import Proyecto


# Register your models here.
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'created_at']