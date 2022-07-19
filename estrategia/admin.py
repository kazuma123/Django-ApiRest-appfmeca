from django.contrib import admin
from estrategia.models import Estrategia


# Register your models here.
@admin.register(Estrategia)
class EstrategiaAdmin(admin.ModelAdmin):
    list_display = ['sigla', 'descripcion', 'created_at','updated_at']

