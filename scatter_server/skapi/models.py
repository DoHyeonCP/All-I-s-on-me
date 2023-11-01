from django.db import models

# Create your models here.
class SkJsonPoisData(models.Model): # 지역
    sk_pois_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add = True)
    
class SKJsonAreasData(models.Model): #상권
    sk_areas_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add = True)