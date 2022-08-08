from django.contrib import admin
from status.models import Status


# Register your models here.
@admin.register(Status)
class PostAdmin(admin.ModelAdmin):
    list_display = ['nombre','created_at']