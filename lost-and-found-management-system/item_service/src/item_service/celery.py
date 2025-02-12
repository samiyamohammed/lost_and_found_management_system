from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'item_service.settings')

app = Celery('item_service')

# Configurations from Django settings
app.config_from_object('django.conf:settings', namespace='CELERY')

# Discover tasks from installed apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
