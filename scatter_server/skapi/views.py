from django.http import JsonResponse
from .models import SKJsonAreasData, SkJsonPoisData

def get_sk_hotspots(request):
    # 데이터베이스에서 혼잡도 데이터를 조회
    areas_data = SKJsonAreasData.objects.all()
    pois_data = SkJsonPoisData.objects.all()

    # 조회한 데이터를 JSON으로 변환하여 반환
    response_data = {
        "areas": list(areas_data.values()),
        "pois": list(pois_data.values())
    }
    return JsonResponse(response_data, safe=False, json_dumps_params={'ensure_ascii': False}, content_type='application/json')






