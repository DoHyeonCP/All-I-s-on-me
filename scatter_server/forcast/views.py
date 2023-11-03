from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view
import os

# 실제 프로덕션 환경에선(DEBUG = False일 때) Django가 직접 서빙하지 않으므로
# Ngnix를 사용하여 미디어파일을 직접 서빙하도록 해야한다.
# 특정 확장자만 반환하고 싶다면 image.endswith('.png') 를 사용해야함
@api_view(['GET'])
def image_list(request):
    # 이미지 파일 목록을 가져옵니다.
    images_directory = settings.MEDIA_ROOT
    images = os.listdir(images_directory)
    image_data = []
    for image in images:
        image_path = request.build_absolute_uri(settings.MEDIA_URL + image)
        # 실제로는 이미지 URL을 생성하여 제공해야 합니다.
        # 예: request.build_absolute_uri(media_url)
        image_data.append(image_path)
    return Response(image_data)