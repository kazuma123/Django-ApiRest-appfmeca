from django.contrib import admin
from tiempo.models import Tiempo


# Register your models here.
@admin.register(Tiempo)
class PostTiempo(admin.ModelAdmin):
    list_display = ['sigla', 'descripcion', 'created_at','updated_at']

