from django.contrib import admin
from models import Domain

# Register your models here.

class DomainAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Domain, DomainAdmin)
