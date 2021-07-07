from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_bot.settings')
app = Celery('price_bot')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {

    # “At every 2 minute.”
    'get_product_price': {
        'task': 'price_bot.tasks.get_product_price',
        'schedule': crontab(minute='*/2')
    },
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
