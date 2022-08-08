from django.contrib import admin
from identificacion.models import Identificacion


# Register your models here.
@admin.register(Identificacion)
class PostAdmin(admin.ModelAdmin):
    list_display = ['fecha_ingreso', 'originador','created_at']
