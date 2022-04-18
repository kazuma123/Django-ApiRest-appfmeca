from django.contrib import admin
from fmeca.models import FMeca


# Register your models here.
@admin.register(FMeca)
class PostAdmin(admin.ModelAdmin):
    list_display = ['ds_modo_falla', 'ds_efecto_falla', 'descripcion_tarea', 'created_at']
