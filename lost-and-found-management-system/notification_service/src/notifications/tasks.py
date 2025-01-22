# from celery import shared_task
# from django.core.mail import send_mail

# @shared_task
# def send_notification(data):
#     user_email = data.get('user_email')
#     subject = data.get('subject')
#     message = data.get('message')
    
#     send_mail(
#         subject,
#         message,
#         'your-email@example.com',
#         [user_email],
#         fail_silently=False,
#     )
    
from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_notification(data):
    user_email = data.get('user_email')  # Extracted dynamically from User Service
    subject = data.get('subject')
    message = data.get('message')
    
    if not user_email:
        print("No email provided. Skipping notification.")
        return
    
    send_mail(
        subject,
        message,
        'no-reply@lostfound.com',  # Use a generic sender email
        [user_email],
        fail_silently=False,
    )
