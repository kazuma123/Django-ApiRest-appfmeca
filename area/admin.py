from django.contrib import admin
from area.models import Area


# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['get_proyects','nombre', 'created_at']

