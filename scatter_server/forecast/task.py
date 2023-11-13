from __future__ import absolute_import, unicode_literals
from celery import shared_task
from forecast_virtual import forecast_virtual  # AI 팀 코드가 함수로 존재한다고 가정

@shared_task
def run_forecast_virtual():
    forecast_virtual()