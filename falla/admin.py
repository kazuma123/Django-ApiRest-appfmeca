from django.contrib import admin
from falla.models import Falla


# Register your models here.
@admin.register(Falla)
class PostAdmin(admin.ModelAdmin):
    list_display = ['maquina_id', 'especialidad_id', 'medida_tiempo_id', 'estrategia_id','falla_funcional','modo_falla']


# @admin.register(MaquinaFmeca)
# class MaquinaFmecaAdmin(admin.ModelAdmin):
#     list_display = ['maquina_id','fmeca_id', 'created_at','updated_at']