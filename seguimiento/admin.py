from django.contrib import admin
from seguimiento.models import Seguimiento


# Register your models here.
@admin.register(Seguimiento)
class PostAdmin(admin.ModelAdmin):
    list_display = ['asignacion', 'fecha_asignacion','created_at']
