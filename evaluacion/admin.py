from django.contrib import admin
from evaluacion.models import Evaluacion


# Register your models here.
@admin.register(Evaluacion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['impacto', 'solucion_propuesta','created_at']
