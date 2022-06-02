from django.contrib import admin
from equipos_completos.models import EquiposCompletos


# Register your models here.
@admin.register(EquiposCompletos)
class EquiposCompletosAdmin(admin.ModelAdmin):
    list_display = ['machine_type']