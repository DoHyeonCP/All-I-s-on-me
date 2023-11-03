from celery import shared_task
from .callapi import UpdateSkAPi
import logging

logger = logging.getLogger(__name__)

@shared_task()
def periodic_update_congestion_data():
    logger.info("Starting to update congestion data.")
    try:
        updater = UpdateSkAPi()
        updater.update_congestion_data()
        logger.info("Finished updating congestion data.")
    except Exception as e:
        logger.error(f"Error updating congestion data: {e}", exc_info=True)




    