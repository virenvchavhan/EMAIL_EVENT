from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
# from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DXL_Auto_Mail.settings')

app = Celery('DXL_Auto_Mail')

app.conf.enable_utc = False
app.conf.update(timezone='Asia/Kolkata')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-mail-at-8':{
        'task':'employee.tasks.send_event_emails',
        # 'task':'employee.tasks.test_func',
        'schedule': crontab(hour=8, minute=00),
    }
}
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: ')

 

# celery -A DXL_Auto_Mail.celery worker --pool=solo -l INFO

# celery -A DXL_Auto_Mail.celery beat --pool=solo -l INFO