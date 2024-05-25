# healthcare_manager/celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'healthcare_manager.settings')

app = Celery('healthcare_manager')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_reminder(email, appointment_date):
    send_mail(
        'Appointment Reminder',
        f'You have an appointment on {appointment_date}',
        'from@example.com',
        [email],
        fail_silently=False,
    )
