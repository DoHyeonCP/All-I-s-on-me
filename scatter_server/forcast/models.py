from django.db import models
# Create your models here.

class ImageFile(models.Model):
    file_name = models.CharField(max_length = 50)
    image = models.ImageField(default = 'AI_nodjango/images/areas.png')