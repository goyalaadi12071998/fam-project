import logging

from celery.schedules import crontab
from celery.task.base import periodic_task

from playground import dal


logger = logging.getLogger(__name__)


@periodic_task(run_every=crontab(minute='*/15'))
def fetch_data_from_youtube():
    try:
        dal.fetch_data_and_save_data_in_db()
    except Exception:
        logger.error('Failed to fetch data from youtube')