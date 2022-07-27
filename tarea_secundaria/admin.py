from django.contrib import admin
from tarea_secundaria.models import TareaSecundaria


# Register your models here.
@admin.register(TareaSecundaria)
class PostAdmin(admin.ModelAdmin):
    list_display = ['descripcion_accion_secundaria', 'duracion_trabajo','personas','repuesto','descripcion_repuesto','procedimiento_trabajo']
