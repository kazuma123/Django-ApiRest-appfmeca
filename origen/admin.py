from django.contrib import admin
from origen.models import Origen


# Register your models here.
@admin.register(Origen)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion','created_at']
