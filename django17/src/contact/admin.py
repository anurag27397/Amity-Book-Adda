from django.contrib import admin

# Register your models here.
from .models import Information

class InfoAdmin(admin.ModelAdmin):
    class Meta:
        models=Information

admin.site.register(Information, InfoAdmin)
