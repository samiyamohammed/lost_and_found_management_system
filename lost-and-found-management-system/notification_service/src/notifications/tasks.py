from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification(data):
    user_email = data.get('user_email')
    subject = data.get('subject')
    message = data.get('message')

    send_mail(
        subject,
        message,
        'your-email@example.com',
        [user_email],
        fail_silently=False,
    )
