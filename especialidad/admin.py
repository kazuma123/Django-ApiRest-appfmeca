from django.contrib import admin
from especialidad.models import Especialidad


# Register your models here.
@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ['siglas', 'descripcion', 'created_at','updated_at']
