from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AreaInfo
from .serializers import AreaInfoDataSerializer

@api_view(['GET'])
def get_sk_hotspots(request):
    # 데이터베이스에서 혼잡도 데이터를 조회
    areas = AreaInfo.objects.all()

     # Serializer를 사용하여 데이터를 JSON으로 직렬화
    areas_serializer = SKJsonAreasDataSerializer(areas_data, many=True)
    pois_serializer = SKJsonPoisDataSerializer(pois_data, many=True)

    # 조회한 데이터를 JSON으로 변환하여 반환
    response_data = {
        "areas": list(areas_data.values()),
        "pois": list(pois_data.values())
    }
    return Response(response_data)






