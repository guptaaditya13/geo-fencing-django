from django.contrib import admin

from .models import GPSData


class GPSDataAdmin(admin.ModelAdmin):
    list_display = ('time', 'latitude', 'longitude')


admin.site.register(GPSData, GPSDataAdmin)
# Register your models here.
