import requests
from django.conf import settings
from celery import shared_task # �񵿱� �۾�ó���� ���� ���̺귯��
from .models import Hotspot

@shared_task
def update_seoul_hotspots():
    startpoint = 1 # ��ŸƮ ����Ʈ, ���Ƿ� �������� �����ؾ���
    endpoint = 6 # ��ŸƮ ����Ʈ, ���Ƿ� �������� �����ؾ���
    api_key = settings.SEOUL_API_KEY
    url =  f'https://api.seoul.go.kr:8088/{api_key}/json/citydata/{startpoint}/{endpoint}'

    response = requests.get(url)
    data = response.json()
    
    hotspots_data = data['hotspots']
    
    for hotspot_data in hotspots_data:
        AREA_NM = hotspot_data['AREA_NM'] 
        LIVE_PPLTN_STTS = hotspot_data['LIVE_PPLTN_STTS']
        AREA_CONGEST_LVL = hotspot_data['AREA_CONGEST_LVL']
        AREA_CONGEST_MSG = hotspot_data['AREA_CONGET_MSG']
        AREA_PPLTN_MIN = hotspot_data['AREA_PPLTN_MIN']
        AREA_PPLTN_MAX = hotspot_data['AREA_PPLTN']
        
        hotspot, created = Hotspot.objects.get_or_create(AREA_NM = AREA_NM)
        hotspot.LIVE_PPLTN_STTS = LIVE_PPLTN_STTS
        hotspot.AREA_CONGEST_LVL = AREA_CONGEST_LVL
        hotspot.AREA_CONGEST_MSG = AREA_CONGEST_MSG
        hotspot.AREA_PPLTN_MIN = AREA_PPLTN_MIN
        hotspot.AREA_PPLTN_MAX = AREA_PPLTN_MAX
        hotspot.save()





# RabbitMQ: RabbitMQ�� ��뷮 ������ ó���� �л� �۾� ó���� ���� ���Ǵ� 
# �޽��� ���Ŀ�Դϴ�. RabbitMQ�� �������� Ȯ�强�� �پ��, �پ��� Ŭ���̾�Ʈ
# ���̺귯���� �����մϴ�.

# Apache Kafka: Apache Kafka�� ���� �л� ��Ʈ���� �÷�������, ��뷮 ������
# ��Ʈ�� ó���� �����մϴ�. Kafka�� �����͸� �ż��ϰ� ó���ϰ� �����ϱ� ���� 
# �޽��� �ý������� ���� �� �ֽ��ϴ�.

# Redis: Redis�� �θ޸� ������ ����ҷ�, �ӵ��� ������ ������ ��������
# ��뷮 ������ ó���� �����մϴ�. Redis�� Pub/Sub ��Ŀ������ �����Ͽ� 
# �������� ���� �� ������ ó���� �� �ֽ��ϴ�. Celery�� �Բ� ���

# mqtt �� ������ �淮�̱� ����