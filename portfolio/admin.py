from django.contrib import admin
from .models import Project, Framework

# Register your models here.

admin.site.register(Project)


@admin.register(Framework)
class FrameworkAdmin(admin.ModelAdmin):
    pass