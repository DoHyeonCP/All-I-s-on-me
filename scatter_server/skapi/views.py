from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import AreaInfo
from .serializers import AreaInfoDataSerializer
from .callapi import UpdateSkAPi

@api_view(['GET'])
def get_sk_hotspots(request):
    try:
        areas = AreaInfo.objects.all()
        serializer = AreaInfoDataSerializer(areas, many = True)
        return Response(serializer.data)
    except Exception as e:
        return Response({"error" "{e}" }, status= 500)





