from django.contrib import admin
from clasificacion.models import Clasificacion


# Register your models here.
@admin.register(Clasificacion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','created_at']
