from django.db import models

class AreaInfo(models.Model):
    area_name = models.CharField(max_length=100, unique=True)
    datetime = models.CharField(max_length=100, unique=True)
    congestion_level = models.CharField(max_length=50)

    def __str__(self):
        return self.area_name