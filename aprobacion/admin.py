from django.contrib import admin
from aprobacion.models import Aprobacion


# Register your models here.
@admin.register(Aprobacion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['aprobador', 'fecha_aprobacion', 'asignado', 'created_at']
