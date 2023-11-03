from django.contrib import admin
from .models import AreaInfo
from django_celery_beat.models import PeriodicTask, IntervalSchedule
# Register your models here.
@admin.register(AreaInfo)
class AreaInfoAdmin(admin.ModelAdmin):
    list_display = ('area_name', 'datetime', 'congestion_level')

