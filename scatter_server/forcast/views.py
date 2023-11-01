from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.

from django.shortcuts import render
import os

def export_images_as_json(request):
    image_folder = 'AI_nodjango/images' # 템플릿 디렉토리 경로

    image_files = os.listdir(image_folder)
    image_data = {}
    for image_file in image_files:
        image_path = os.path.join(image_file, image_folder)
        image_data[image_file] = {'path': image_path}
        
    return JsonResponse(image_data, safe = False)