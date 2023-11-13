import os
from django.db import models
from django.conf import settings
# Create your models here.

class ImageFile(models.Model):
    file_name = models.CharField(max_length = 50)
    image = models.ImageField(default = os.path.join(settings.MEDIA_ROOT, "/forecast_image"))