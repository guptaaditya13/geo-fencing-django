from django.db import models


class GPSData(models.Model):
    time = models.DateTimeField(auto_now=True, auto_created=True)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
# Create your models here.
