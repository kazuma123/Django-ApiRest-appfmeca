from django.contrib import admin
from area.models import Area


# Register your models here.
@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'created_at']
