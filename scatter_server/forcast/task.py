from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .forcast_virtulization.main import forcast_virtual  # AI 팀 코드가 함수로 존재한다고 가정

@shared_task
def run_ai_script():
    forcast_virtual()