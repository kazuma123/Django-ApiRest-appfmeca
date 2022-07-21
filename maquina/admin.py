from django.contrib import admin
from maquina.models import Maquina


# Register your models here.
@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):
    list_display = ['machine_type', 'description_machine_type','funcion','created_at','updated_at']

