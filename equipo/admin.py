from django.contrib import admin
from equipo.models import Equipo


# Register your models here.
@admin.register(Equipo)
class PostAdmin(admin.ModelAdmin):
    list_display = ['tag', 'nombre', 'created_at','updated_at']

