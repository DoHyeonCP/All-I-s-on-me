from rest_framework import serializers
from .models import AreaInfo

class AreaInfoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaInfo
        fields = '__all__'