from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Définir les paramètres Django pour Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_tracker.settings')

# Créer une instance Celery
app = Celery('fitness_tracker', broker='redis://localhost:6380/0')

# Charger les paramètres de configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# Découvrir automatiquement les tâches dans toutes les applications listées dans INSTALLED_APPS
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
