import requests
import xml.etree.ElementTree as ET
from django.conf import settings
from celery import shared_task # �񵿱� �۾�ó���� ���� ���̺귯��
# from .models import Hotspot

# Use, later(auto callback function)
# @shared_task
# def update_seoul_hotspots():
#     startpoint = 1 # ��ŸƮ ����Ʈ, ���Ƿ� �������� �����ؾ���
#     endpoint = 6 # ��ŸƮ ����Ʈ, ���Ƿ� �������� �����ؾ���
#     api_key = settings.SEOUL_API_KEY
#     url =  f'https://api.seoul.go.kr:8088/{api_key}/json/citydata/{startpoint}/{endpoint}'

#     response = requests.get(url)
#     hotspots_data = response.content
    
#     root = ET.fromstring(hotspots_data)
    
#     # for hotspot_data in root.iter('hotspot'):
#     AREA_NM = root.find('CITYDATA/AREA_NM').text
#     LIVE_PPLTN_STTS = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS').text
#     AREA_CONGEST_LVL = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/AREA_CONGEST_LVL').text
#     AREA_CONGEST_MSG = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/AREA_CONGEST_MSG').text
#     AREA_PPLTN_MIN = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/AREA_PPLTN_MIN').text
#     AREA_PPLTN_MAX = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/AREA_PPLTN_MAX').text
#     MALE_PPLTN_RATE = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/MALE_PPLTN_RATE').text
#     FEMALE_PPLTN_RATE = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/FEMALE_PPLTN_RATE').text
#     PPLTN_RATE_0 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_0').text
#     PPLTN_RATE_10 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_10').text
#     PPLTN_RATE_20 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_20').text
#     PPLTN_RATE_30 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_30').text
#     PPLTN_RATE_40 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_40').text
#     PPLTN_RATE_50 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_50').text
#     PPLTN_RATE_60 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_60').text
#     PPLTN_RATE_70 = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_RATE_70').text
#     RESNT_PPLTN_RATE = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/RESNT_PPLTN_RATE').text
#     NON_RESNT_PPLTN_RATE = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/NON_RESNT_PPLTN_RATE').text
#     REPLACE_YN = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/REPLACE_YN').text
#     PPLTN_TIME = root.find('CITYDATA/LIVE_PPLTN_STTS/LIVE_PPLTN_STTS/PPLTN_TIME').text
    
#     hotspot = Hotspot.objects.create(
#     AREA_NM = AREA_NM,
#     LIVE_PPLTN_STTS = LIVE_PPLTN_STTS,
#     AREA_CONGEST_LVL = AREA_CONGEST_LVL,
#     AREA_CONGEST_MSG = AREA_CONGEST_MSG,
#     AREA_PPLTN_MIN = AREA_PPLTN_MIN,
#     AREA_PPLTN_MAX = AREA_PPLTN_MAX,
#     MALE_PPLTN_RATE = MALE_PPLTN_RATE,
#     FEMALE_PPLTN_RATE = FEMALE_PPLTN_RATE,
#     PPLTN_RATE_0 = PPLTN_RATE_0,
#     PPLTN_RATE_10 = PPLTN_RATE_10,
#     PPLTN_RATE_20 = PPLTN_RATE_20,
#     PPLTN_RATE_30 = PPLTN_RATE_30,
#     PPLTN_RATE_40 = PPLTN_RATE_40,
#     PPLTN_RATE_50 = PPLTN_RATE_50,
#     PPLTN_RATE_60 = PPLTN_RATE_60,
#     PPLTN_RATE_70 = PPLTN_RATE_70,
#     RESNT_PPLTN_RATE = RESNT_PPLTN_RATE,
#     NON_RESNT_PPLTN_RATE = NON_RESNT_PPLTN_RATE,
#     REPLACE_YN = REPLACE_YN,
#     PPLTN_TIME = PPLTN_TIME 
#     )    
#     hotspot.save()





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