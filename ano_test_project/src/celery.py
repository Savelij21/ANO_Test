import os
from celery import Celery
from celery.signals import setup_logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.settings')

app = Celery('ano_test')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()  # looking for tasks in project


@setup_logging.connect
def config_loggers(*args, **kwargs) -> None:
    from logging.config import dictConfig
    from django.conf import settings

    dictConfig(settings.LOGGING)

