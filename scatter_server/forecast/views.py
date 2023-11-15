from django.shortcuts import render
from django.conf import settings
import os
import re
from datetime import datetime


def forecast(request):
    directory_path = os.path.join(settings.MEDIA_ROOT, "forecast_image")
    images = [f for f in os.listdir(directory_path) if f.startswith('areas_') and f.endswith('.png')]
    
    formatted_images = []
    for filename in images:
        match = re.search(r'areas_(\d{2})(\d{2})\.png', filename)
        if match:
            month = int(match.group(1))
            day = int(match.group(2))
            date_str = f"{month}월 {day}일"
            formatted_images.append((filename, date_str))
        else:
            formatted_images.append((filename, filename))
    
    return render(request, 'forecast.html', {'images': formatted_images})
