#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class SeoulJsonData(models.Model):
    area_nm = models.CharField(max_length = 255)
    seoul_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.data)
    
class SkJsonPoisAreasHourData(models.Model): # �ð��뺰
	sk_pois_hour_data = models.JSONField()
	sk_areas_hour_data = models.JSONField()
	created_at = models.DateTimeField(auto_now_add = True)
   
   
   
# �ʿ� �������� ����� ������ ���� ���� 06.15 
class SkJsonPoisData(models.Model): # ����
    sk_pois_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add = True)
    
class SKJsonAreasData(models.Model): #���
    sk_areas_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add = True)


    
    
    

# json�м� �� ���۵� ��
# class Hotspot(models.Model):
#     AREA_NM = models.CharField(max_length= 20) # �ֽ��� ��Ҹ�
#     LIVE_PPLTN_STTS = models.CharField(max_length = 255, null = True) # �ǽð� �α���Ȳ
#     AREA_CONGEST_LVL = models.CharField(max_length = 10) # ��� ȥ�⵵ ��ǥ
#     AREA_CONGEST_MSG = models.CharField(max_length=255) # ��� ȥ�⵵ ���� �޼���
#     AREA_PPLTN_MIN = models.IntegerField() # �ǽð� �α� ��ǥ �ּҰ�
#     AREA_PPLTN_MAX = models.IntegerField() # �ǽð� �α� ��ǥ �ִ밪
#     MALE_PPLTN_RATE = models.FloatField() #  ���� �α� ����
#     FEMALE_PPLTN_RATE = models.FloatField() # ���� �α� ����
#     PPLTN_RATE_0 = models.FloatField() # 0 ~ 10�� �α�����
#     PPLTN_RATE_10 = models.FloatField() # 10�� �α�����
#     PPLTN_RATE_20 = models.FloatField() # 20�� �α�����
#     PPLTN_RATE_30 = models.FloatField() # 30�� �α�����
#     PPLTN_RATE_40 = models.FloatField() # 40�� �α�����
#     PPLTN_RATE_50 = models.FloatField() # 50�� �α�����
#     PPLTN_RATE_60 = models.FloatField() # 60�� �α�����
#     PPLTN_RATE_70 = models.FloatField() # 70�� �α�����
#     RESNT_PPLTN_RATE = models.FloatField() # ���� �α�����(������)
#     NON_RESNT_PPLTN_RATE = models.FloatField() #����� �α�����(�� ������)
#     REPLACE_YN = models.CharField(max_length = 2) # ��ü ������ ����
#     PPLTN_TIME = models.DateTimeField() # �ǽð� �α� ������ ������Ʈ �ð�
#     ROAD_TRAFFIC_STTS = models.CharField(max_length = 255, null = True)#���μ�����Ȳ
#     ROAD_TRAFFIC_SPD = models.IntegerField	#��ü���μ�����ռӵ�
#     ROAD_TRAFFIC_IDX = models.CharField(max_length = 10)	#��ü���μ��������Ȳ
#     ROAD_TRAFFIC_TIME = models.DateTimeField	#���μ�����Ȳ ������Ʈ �ð�
#     ROAD_MSG = models.CharField(max_length=255)	#��ü���μ��������Ȳ �޼���
#     LINK_ID = models.IntegerField()	#���α��� LINK ID
#     ROAD_NM = models.CharField(max_length = 20)	#���θ�
#     START_ND_CD = models.IntegerField()	#���γ��������� �ڵ�
#     START_ND_NM = models.CharField(max_length = 255)	#���γ����۸�
#     START_ND_XY = models.FloatField()	#���γ�����������ǥ
#     END_ND_CD = models.IntegerField()	#���γ���������� �ڵ�
#     END_ND_NM = models.CharField(max_length= 255)	#���γ�������
#     END_ND_XY = models.FloatField()	#���γ������������ǥ
#     DIST = models.IntegerField()	#���α�������
#     SPD = models.FloatField()	#���α�����ռӵ�
#     IDX = models.CharField(max_length = 255)	#���α���������ǥ
#     XYLIST = models.FloatField()	#��ũ���̵� ��ǥ(������)
#     PRK_STTS = models.CharField(max_length = 255, null = True)	#������ ��Ȳ
#     PRK_NM = models.CharField(max_length = 255)	#�������
#     PRK_CD = models.IntegerField()	#�������ڵ�
#     CPCTY = models.FloatField()	#������ ���� ���� ���
#     CUR_PRK_CNT = models.FloatField()	#������ ���� ���� ���
#     CUR_PRK_TIME = models.DateTimeField()	#���� ������ ���� ���� �� ������Ʈ �ð�
#     CUR_PRK_YN = models.CharField(max_length = 2)	#�ǽð� ������ ���� ��Ȳ ���� ����
#     PAY_YN = models.CharField(max_length = 2)	#������ ����
#     RATES = models.IntegerField()	#�⺻�������
#     TIME_RATES = models.IntegerField()	#�⺻���������ð�
#     ADD_RATES = models.IntegerField	#�߰������������
#     ADD_TIME_RATES = models.IntegerField()	#�߰����������ð�
#     ROAD_ADDR = models.CharField(max_length = 30)	#���θ��ּ�
#     LAT = models.FloatField()	#����
#     LNG = models.FloatField()	#�浵
#     SUB_STTS = models.CharField(max_length = 255, null = True)	#����ö �ǽð� ���� ��Ȳ
#     SUB_STN_NM = models.CharField(max_length = 30)	#����ö����
#     SUB_STN_LINE = models.CharField(max_length = 10)	#����ö�� ȣ��
#     SUB_STN_RADDR = models.CharField(max_length = 255)	#����ö�� ���θ� �ּ�
#     SUB_STN_JIBUN = models.CharField(max_length = 255)	#����ö�� �� �����ּ�
#     SUB_STN_X = models.FloatField()	#����ö�� X ��ǥ(�浵)
#     SUB_STN_Y = models.FloatField()	#����ö�� Y ��ǥ(����)
#     SUB_NT_STN = models.IntegerField()	#������ �ڵ�
#     SUB_BF_STN = models.IntegerField()	#������ �ڵ�
#     SUB_ROUTE_NM = models.CharField(max_length = 10)	#����ö�뼱��
#     SUB_LINE = models.CharField(max_length = 10)	#����öȣ��
#     SUB_ORD = models.CharField(max_length = 255)	#����������������
#     SUB_DIR = models.CharField(max_length = 5)	#����ö����
#     SUB_TERMINAL = models.CharField(max_length = 255)#������
#     SUB_ARVTIME = models.CharField(max_length = 50)	#���� ���� �ð�
#     SUB_ARMG1 = models.CharField(max_length = 255)	#���� ���� �޼���
#     SUB_ARMG2 = models.CharField(max_length = 255)	#���� ���� �޼���
#     SUB_ARVINFO = models.IntegerField()	#���� ���� �ڵ� ����
#     BUS_STN_STTS = models.CharField(max_length = 255)	#���������� ��Ȳ
#     BUS_STN_ID = models.IntegerField()	#������ID
#     BUS_ARD_ID = models.IntegerField()	#������ ������ȣ
#     BUS_STN_NM = models.CharField(max_length =255)	#�����Ҹ�
#     BUS_STN_X = models.FloatField()	#������ X ��ǥ(�浵)
#     BUS_STN_Y = models.FloatField()	#������ Y ��ǥ(����)
#     RTE_STN_NM = models.CharField(max_length = 255)	#�뼱 ��ȸ ���� �������
#     RTE_NM = models.CharField(max_length = 255)	#�뼱��
#     RTE_ID = models.IntegerField()	#�뼱ID
#     RTE_SECT = models.CharField(max_length = 255)	#�뼱����
#     RTE_CONGEST = models.CharField(max_length = 255)	#�뼱ȥ�⵵
#     RTE_ARRV_TM	 = models.TimeField()#�뼱�������ð�
#     RTE_ARRV_STN = models.CharField(max_length = 255)	#�뼱�ֱٵ���������
#     ACDNT_CNTRL_STTS = models.CharField(max_length = 255, null = True)	#���������Ȳ
#     ACDNT_OCCR_DT = models.DateTimeField()	#���߻��Ͻ�
#     EXP_CLR_DT = models.DateTimeField()	#�������Ό���Ͻ�
#     ACDNT_TYPE = models.CharField(max_length = 20)	#���߻�����
#     ACDNT_DTYPE = models.CharField(max_length =20)	#���߻���������
#     ACDNT_INFO = models.CharField(max_length = 50)	#�����������
#     ACDNT_X = models.FloatField()	#����������� X ��ǥ
#     ACDNT_Y	 = models.FloatField()#����������� Y ��ǥ
#     ACDNT_TIME = models.TimeField()	#���������Ȳ ������Ʈ �ð�
#     SBIKE_STTS = models.CharField(max_length = 255, null = True)	#������ ��Ȳ
#     SBIKE_SPOT_NM = models.CharField(max_length = 50)	#�����̴뿩�Ҹ�
#     SBIKE_SPOT_ID = models.IntegerField()	#�����̴뿩��ID
#     SBIKE_SHARED = models.FloatField()	#�����̰�ġ��
#     SBIKE_PARKING_CNT = models.IntegerField()	#������ ���� �Ǽ�
#     SBIKE_RACK_CNT = models.IntegerField()	#�����̰�ġ�� ����
#     SBIKE_X = models.FloatField()	#�����̴뿩�� ��ǥ �浵
#     SBIKE_Y = models.FloatField()	#�����̴뿩�� ��ǥ ����
#     WEATHER_STTS = models.CharField(max_length= 1, null = True)	#���� ��Ȳ
#     TEMP = models.FloatField()	#���
#     SENSIBLE_TEMP = models.FloatField()	#ü���µ�
#     MAX_TEMP = models.FloatField()	#�� �����µ�/�ְ�µ�
#     MIN_TEMP = models.FloatField()	#�� �����µ�/�ְ�µ�
#     HUMIDITY = models.FloatField()	#����
#     WIND_DIRCT = models.CharField(max_length = 10)	#ǳ��
#     WIND_SPD = models.FloatField()	#ǳ��
#     PRECIPITATION = models.FloatField()	#������
#     PRECPT_TYPE = models.CharField(max_length = 50)	#��������
#     PCP_MSG = models.CharField(max_length = 255)	#�������� �޼���
#     SUNRISE = models.TimeField()	#����ð�
#     SUNSET = models.TimeField()	#�ϸ��ð�
#     UV_INDEX_LVL = models.IntegerField()	#�ڿܼ����� �ܰ�
#     UV_INDEX = models.CharField(max_length = 20)	#�ڿܼ�����
#     UV_MSG = models.CharField(max_length = 50)	#�ڿܼ��޼���
#     PM25_INDEX = models.CharField(max_length = 50)	#�ʹ̼�������ǥ
#     PM25 = models.FloatField()	#�ʹ̼�������
#     PM10_INDEX = models.CharField(max_length = 20)	#�̼�������ǥ
#     PM10 = models.FloatField()	#�̼�������
#     AIR_IDX = models.CharField(max_length = 20)	#���մ��ȯ����
#     AIR_IDX_MVL = models.FloatField()	#���մ��ȯ������
#     AIR_IDX_MAIN = models.CharField(max_length = 10)	#���մ��ȯ������ ��������
#     AIR_MSG = models.CharField(max_length = 50)	#���մ��ȯ���޺� �޼���
#     WEATHER_TIME = models.DateTimeField()	#���� ������ ������Ʈ �ð�
#     NEWS_LIST = models.CharField(max_length = 50, null = True)	#������Ư��
#     WARN_VAL = models.CharField(max_length = 50, null = True)	#���Ư������
#     WARN_STRESS	 = models.CharField(max_length = 50, null = True)#���Ư������
#     ANNOUNCE_TIME = models.DateTimeField(null = True)	#���Ư����ȿ�ð�
#     COMMAND = models.IntegerField()	#���Ư����ǥ�ڵ�
#     CANCEL_YN = models.CharField(max_length = 10, null = True)	#���Ư����ұ���
#     WARN_MSG = models.CharField(max_length = 255, null = True)	#���Ư���� �ൿ����
#     FCST24HOURS = models.CharField(max_length = 1, null = True)	#24�ð� ����
#     FCST_DT = models.DateTimeField()	#�����ð�
#     TEMP = models.FloatField()	#���
#     PRECIPITATION = models.IntegerField()	#������
#     PRECPT_TYPE = models.CharField(max_length = 255)	#��������
#     RAIN_CHANCE = models.FloatField()	#����Ȯ��
#     SKY_STTS = models.CharField(max_length =255)	#�ϴû���
#     COVID_19_STTS = models.CharField(max_length = 255, null = True)	#�ڷγ�19 ��Ȳ
#     STRD_DT = models.DateTimeField()	#������
#     GU_NM = models.CharField(max_length= 50)	#������ ��ġ����
#     GU_CONFIRMED = models.IntegerField()	#(��ġ��)Ȯ���� ��
#     GU_ADDED = models.IntegerField()	#(��ġ��)Ȯ���� �߰�
#     CONFIRMED = models.IntegerField()	#���� ��ü Ȯ���� ��
#     ADDED = models.IntegerField()	#���� ��ü Ȯ���� �߰� ��
#     DIED = models.IntegerField()	#����� ��ü ����� ��
#     T_DIED = models.IntegerField()	#����� ���� ����� ��
 
  # ������������ ����� �� �׾��
	# ROAD_TRAFFIC_STTS	
    # ROAD_TRAFFIC_SPD	
	# ROAD_TRAFFIC_IDX	
	# ROAD_TRAFFIC_TIME	
	# ROAD_MSG	
	# LINK_ID	
	# ROAD_NM	
	# START_ND_CD	
	# START_ND_NM	
	# START_ND_XY	
	# END_ND_CD
	# END_ND_NM	
	# END_ND_XY	
	# DIST	
	# SPD	
	# IDX	
	# XYLIST	
	# PRK_STTS	
	# PRK_NM	
	# PRK_CD	
	# CPCTY	
	# CUR_PRK_CNT	
	# CUR_PRK_TIME	
	# CUR_PRK_YN	
	# PAY_YN	
	# RATES	
	# TIME_RATES	
	# ADD_RATES	
	# ADD_TIME_RATES	
	# ROAD_ADDR	
	# LAT	
	# LNG	
	# SUB_STTS	
	# SUB_STN_NM	
	# SUB_STN_LINE	
	# SUB_STN_RADDR	
	# SUB_STN_JIBUN	
	# SUB_STN_X	
	# SUB_STN_Y	
	# SUB_NT_STN	
	# SUB_BF_STN	
	# SUB_ROUTE_NM	
	# SUB_LINE	
	# SUB_ORD	
	# SUB_DIR	
	# SUB_TERMINAL	
	# SUB_ARVTIME	
	# SUB_ARMG1	
	# SUB_ARMG2	
	# SUB_ARVINFO	
	# BUS_STN_STTS	
	# BUS_STN_ID	
	# BUS_ARD_ID	
	# BUS_STN_NM	
	# BUS_STN_X	
	# BUS_STN_Y	
	# RTE_STN_NM	
	# RTE_NM	
	# RTE_ID	
	# RTE_SECT	
	# RTE_CONGEST	
	# RTE_ARRV_TM	
	# RTE_ARRV_STN	
	# ACDNT_CNTRL_STTS	
	# ACDNT_OCCR_DT	
	# EXP_CLR_DT	
	# ACDNT_TYPE	
	# ACDNT_DTYPE	
	# ACDNT_INFO	
	# ACDNT_X	
	# ACDNT_Y	
	# ACDNT_TIME	
	# SBIKE_STTS	
	# SBIKE_SPOT_NM	
	# SBIKE_SPOT_ID	
	# SBIKE_SHARED	
	# SBIKE_PARKING_CNT
	# SBIKE_RACK_CNT	
	# SBIKE_X
	# SBIKE_Y
	# WEATHER_STTS
	# TEMP	#���
	# SENSIBLE_TEMP
	# MAX_TEMP
	# MIN_TEMP
	# HUMIDITY
	# WIND_DIRCT	
	# WIND_SPD	
	# PRECIPITATION	
	# PRECPT_TYPE	
	# PCP_MSG	
	# SUNRISE	
	# SUNSET	
	# UV_INDEX_LVL	
	# UV_INDEX	
	# UV_MSG	
	# PM25_INDEX	
	# PM25	
	# PM10_INDEX	
	# PM10	
	# AIR_IDX	
	# AIR_IDX_MVL	
	# AIR_IDX_MAIN	
	# AIR_MSG	
	# WEATHER_TIME	
	# NEWS_LIST	
	# WARN_VAL	
	# WARN_STRESS	
	# ANNOUNCE_TIME	
	# COMMAND	
	# CANCEL_YN	
	# WARN_MSG	
	# FCST24HOURS	
	# FCST_DT	
	# TEMP	
	# PRECIPITATION	
	# PRECPT_TYPE	
	# RAIN_CHANCE	
	# SKY_STTS	
	# COVID_19_STTS	
	# STRD_DT	
	# GU_NM	
	# GU_CONFIRMED
	# GU_ADDED
	# CONFIRMED
	# ADDED
	# DIED
	# T_DIED