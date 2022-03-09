from __future__ import absolute_import
import os
import time
from celery import Celery, shared_task
from celery.utils.log import get_task_logger
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")
app = Celery("ratings")
app.config_from_object("django.conf:settings")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

logger = get_task_logger(__name__)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))


@shared_task(name="sleep_task")
def sleep_task():
    logger.info("sleep task")
    print("sleeping")
    time.sleep(10)
    return ""
