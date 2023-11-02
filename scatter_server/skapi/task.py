from celery import shared_task
from callapi import update_congestion_data_batch

@shared_task
def periodic_upadate_congetion_data():
    update_congestion_data_batch()